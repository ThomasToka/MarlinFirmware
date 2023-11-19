### based on https://github.com/dsdanielko/cura-ringing-tower-script/
### created for E3S1PROFORKBYTT by Thomas Toka for Cura Slicer

import json
import re

from ..Script import Script

class E3S1PROFORKBYTT_InputShaping(Script):
    def __init__(self):
        super().__init__()

    def getSettingDataString(self):
        return json.dumps({
            'name': 'E3S1PROFORKBYTT InputShaping',
            'key': 'E3S1PROFORKBYTT InputShaping',
            'metadata': {},
            'version': 2,
            'settings': {
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
                'start_f': {
                    'label': 'Start frequency',
                    'description': 'Ringing compensation frequency sweep start value',
                    'unit': 'Hz',
                    'type': 'int',
                    'default_value': 20
                },
                'end_f': {
                    'label': 'End frequency',
                    'description': 'Ringing compensation frequency sweep end value',
                    'unit': 'Hz',
                    'type': 'int',
                    'default_value': 60
                },
                'linear_advance_k': {
                    'label': 'Reenable LA after Test with K',
                    'description': 'Reenable LA after Test with K',
                    'unit': '',
                    'type': 'float',
                    'default_value': 0.03
                }
            }
        })

    def execute(self, data):
        gc = self.getSettingValueByKey('gcode')
        start_hz = self.getSettingValueByKey('start_f')
        end_hz = self.getSettingValueByKey('end_f')
        linear_advance_k = self.getSettingValueByKey('linear_advance_k')
        linear_advance_disabled = False

        for i, layer in enumerate(data):
            lines = layer.split('\n')
            for j, line in enumerate(lines):
                if line.startswith(";LAYER_COUNT:"):
                    max_layer = float(line.strip(';LAYER_COUNT:'))
                elif line.startswith(';LAYER:'):
                    layer = float(line.strip(';LAYER:'))
                    hz = 0 if layer < 2 else start_hz + (end_hz - start_hz) * (layer - 2) / (max_layer - 3)
                    if gc == 'ftm':
                        if layer == 0:
                            lines[j] += '\n;TYPE:INPUTSHAPING\nM493 S11 D0 ;Enable ZVD Input Shaping'
                        lines[j] += '\n;TYPE:INPUTSHAPING\nM493 A%f ;(Hz) X Input Shaping Test' % hz
                        lines[j] += '\nM493 B%f ;(Hz) Y Input Shaping Test' % hz
                    if gc == 'is':
                        if not linear_advance_disabled:
                            lines[j] = 'M900 K0 ;disable Linear Advance\n' + lines[j]
                            linear_advance_disabled = True
                        lines[j] += '\n;TYPE:INPUTSHAPING\nM593 F%f ;(Hz) Input Shaping Test' % hz
            data[i] = '\n'.join(lines)

        # Re-enable Linear Advance with the specified K-factor after the last line
        data[-1] += '\nM900 K%f ;re-enable Linear Advance with specified K-factor\n' % linear_advance_k

        return data