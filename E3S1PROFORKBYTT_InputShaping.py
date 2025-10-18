### based on https://github.com/dsdanielko/cura-ringing-tower-script/
### created for E3S1PROFORKBYTT by Thomas Toka for Cura Slicer

import json
import re

from ..Script import Script

class E3S1PROFORKBYTT_InputShaping(Script):
    def __init__(self):
        super().__init__()

    def getSettingDataString(self):
        # NOTE: Cura's PostProcessingPlugin UI is static; we can't hide TAU dynamically.
        # We label it as "smooth only" and ignore it on "classic" in execute().
        return json.dumps({
            "name": "E3S1PROFORKBYTT InputShaping",
            "key": "E3S1PROFORKBYTT_InputShaping",
            "metadata": {},
            "version": 2,
            "settings": {
                "gcode": {
                    "label": "Motion planning type",
                    "description": "Use either M593 (ZV input shaping) or M493 (Fixed-time motion)",
                    "type": "enum",
                    "options": {
                        "is": "M593 (ZV Input Shaping)",
                        "ftm": "M493 (Fixed-Time Motion)"
                    },
                    "default_value": "is"
                },
                "forkversion": {
                    "label": "Linear advance version",
                    "description": "Select classic LA (no TAU) or smooth LA (supports TAU)",
                    "type": "enum",
                    "options": {
                        "classic": "classic LA (without TAU) up to v033 and as of v036",
                        "smooth": "smooth LA (with TAU) for v034 and v035"
                    },
                    "default_value": "classic"
                },
                "start_f": {
                    "label": "Start frequency",
                    "description": "Ringing compensation frequency sweep start value",
                    "unit": "Hz",
                    "type": "int",
                    "default_value": 20
                },
                "end_f": {
                    "label": "End frequency",
                    "description": "Ringing compensation frequency sweep end value",
                    "unit": "Hz",
                    "type": "int",
                    "default_value": 100
                },
                "linear_advance_k": {
                    "label": "Re-enable LA after test with K",
                    "description": "K value to restore after the test",
                    "type": "float",
                    "default_value": 0.035
                },
                "linear_advance_tau": {
                    "label": "Linear Advance U (TAU) for smooth linear advance",
                    "description": "Ignored when classic linear advance chosen",
                    "type": "float",
                    "default_value": 0.020
                },
                "input_shaping_hz_x": {
                    "label": "Re-enable input shaping X with",
                    "description": "Input shaping X frequency (Hz) to restore after the test",
                    "unit": "Hz",
                    "type": "float",
                    "default_value": 40.0
                },
                "input_shaping_hz_y": {
                    "label": "Re-enable input shaping Y with",
                    "description": "Input shaping Y frequency (Hz) to restore after the test",
                    "unit": "Hz",
                    "type": "float",
                    "default_value": 40.0
                }
            }
        })

    def execute(self, data):
        # Normalize mode (Cura may return key or label)
        gc_raw = str(self.getSettingValueByKey("gcode")).strip().lower()
        if gc_raw in ("is", "m593 (zv input shaping)", "m593"):
            gc = "is"
        elif gc_raw in ("ftm", "m493 (fixed-time motion)", "m493"):
            gc = "ftm"
        else:
            gc = "is"  # safe default

        forkversion = str(self.getSettingValueByKey("forkversion")).strip().lower()

        # Cast numeric settings safely
        try:
            start_hz = float(self.getSettingValueByKey("start_f"))
        except Exception:
            start_hz = 20.0
        try:
            end_hz = float(self.getSettingValueByKey("end_f"))
        except Exception:
            end_hz = 100.0
        try:
            linear_advance_k = float(self.getSettingValueByKey("linear_advance_k"))
        except Exception:
            linear_advance_k = 0.035
        try:
            linear_advance_tau = float(self.getSettingValueByKey("linear_advance_tau"))
        except Exception:
            linear_advance_tau = 0.020
        try:
            ishz_x = float(self.getSettingValueByKey("input_shaping_hz_x"))
        except Exception:
            ishz_x = 40.0
        try:
            ishz_y = float(self.getSettingValueByKey("input_shaping_hz_y"))
        except Exception:
            ishz_y = 40.0

        # Ensure sweep bounds make sense
        if end_hz < start_hz:
            start_hz, end_hz = end_hz, start_hz  # swap if user inverted them

        linear_advance_disabled = False
        max_layer = 0

        for i, layer in enumerate(data):
            lines = layer.split("\n")
            for j, line in enumerate(lines):
                # Capture total layer count from header
                if line.startswith(";LAYER_COUNT:"):
                    try:
                        max_layer = int(line.replace(";LAYER_COUNT:", "").strip())
                    except ValueError:
                        pass
                    continue

                # Per-layer handling
                if line.startswith(";LAYER:"):
                    try:
                        layer_num = int(line.replace(";LAYER:", "").strip())
                    except ValueError:
                        continue

                    # Sweep mapping:
                    # - Layers 0–1 => F=0 (prime/purge and initial layer)
                    # - Layers 2..(max_layer-1) distributed from start_hz..end_hz
                    if layer_num < 2 or max_layer <= 3:
                        hz = 0.0
                    else:
                        span = max(1, (max_layer - 3))
                        hz = start_hz + (end_hz - start_hz) * (layer_num - 2) / span

                    # Emit commands based on mode
                    if gc == "ftm":
                        if layer_num == 0:
                            lines[j] += "\n;TYPE:INPUTSHAPING\nM493 S11 D0 ; Enable ZVD Input Shaping"
                        lines[j] += f"\n;TYPE:INPUTSHAPING\nM493 A{hz:.2f} ; (Hz) X Input Shaping Test"
                        lines[j] += f"\nM493 B{hz:.2f} ; (Hz) Y Input Shaping Test"

                    elif gc == "is":
                        # Disable Linear Advance once at first encountered layer
                        if not linear_advance_disabled:
                            if forkversion == "smooth":
                                # smooth supports TAU with M900
                                lines[j] = "M900 K0 U0 ; disable Linear Advance\n" + lines[j]
                            else:
                                lines[j] = "M900 K0 ; disable Linear Advance\n" + lines[j]
                            linear_advance_disabled = True

                        lines[j] += f"\n;TYPE:INPUTSHAPING\nM593 F{hz:.2f} ; (Hz) Input Shaping Test"

            data[i] = "\n".join(lines)

        # Re-enable Linear Advance on the very last chunk
        if forkversion == "smooth":
            data[-1] += (
                f"\nM900 K{linear_advance_k:.3f} U{linear_advance_tau:.3f} "
                f"; re-enable Linear Advance with specified K and U"
            )
        else:
            data[-1] += (
                f"\nM900 K{linear_advance_k:.3f} "
                f"; re-enable Linear Advance with specified K (TAU unsupported in classic)"
            )

        # >>> Restore Input Shaping AFTER LA is restored (both modes)
        if gc == "is":
            # Per-axis restore for M593 (adjust to your firmware if global only)
            data[-1] += (
                f"\n; restore input shaping after test"
                f"\nM593 X F{ishz_x:.2f} ; restore X input shaping"
                f"\nM593 Y F{ishz_y:.2f} ; restore Y input shaping\n"
            )
        elif gc == "ftm":
            data[-1] += (
                f"\n; restore input shaping after test"
                f"\nM493 A{ishz_x:.2f} ; restore X input shaping"
                f"\nM493 B{ishz_y:.2f} ; restore Y input shaping\n"
            )

        return data


