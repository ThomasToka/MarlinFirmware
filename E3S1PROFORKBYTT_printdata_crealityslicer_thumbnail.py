#------------------------------------------------------------------------------
# Cura 5.4 JPEG Thumbnail creator
#
# This script has been changed for E3S1PROFORKBYTT by Thomas Toka.
#
# Intruduced with v008 into E3S1PROFORKBYTT.
#
# It is based on the modification of:
#
# Professional firmware for Ender3v2
# Miguel A. Risco-Castillo
# version: 1.4
# date: 2022-05-18
#
# Contains code from:
# https://github.com/Ultimaker/Cura/blob/master/plugins/PostProcessingPlugin/scripts/CreateThumbnail.py
#------------------------------------------------------------------------------


import base64
import math
import re
from UM.Logger import Logger
from cura.Snapshot import Snapshot
from cura.CuraVersion import CuraVersion
from ..Script import Script
from UM.Application import Application
from PyQt5.QtCore import QByteArray, QIODevice, QBuffer
from PyQt5.QtGui import QDesktopServices

class E3S1PROFORKBYTT_printdata_crealityslicer_thumbnail(Script):
    def __init__(self):
        super().__init__()

    def _createSnapshot(self, width, height):
        Logger.log("d", "Creating thumbnail image...")
        try:
            return Snapshot.snapshot(width, height)
        except Exception as e:
            Logger.logException("w", "Failed to create snapshot image. Error: {}".format(str(e)))

    def _encodeSnapshot(self, snapshot):
        #from PyQt5.QtCore import QByteArray, QBuffer
        Major=0
        try:
          Major = int(CuraVersion.split(".")[0])
        except:
          pass

        if Major < 5 :
          from PyQt5.QtCore import QByteArray, QIODevice, QBuffer
        else :
          from PyQt6.QtCore import QByteArray, QIODevice, QBuffer

        Logger.log("d", "Encoding thumbnail image...")
        try:
            thumbnail_buffer = QBuffer()
            if Major < 5 :
              thumbnail_buffer.open(QBuffer.ReadWrite)
            else:
              thumbnail_buffer.open(QBuffer.OpenModeFlag.ReadWrite)
            snapshot.save(thumbnail_buffer, "JPG")
            base64_bytes = base64.b64encode(thumbnail_buffer.data())
            base64_message = base64_bytes.decode('ascii')
            thumbnail_buffer.close()
            return base64_message
        except Exception as e:
            Logger.logException("w", "Failed to encode snapshot image. Error: {}".format(str(e)))

    def _convertSnapshotToGcode(self, encoded_snapshot, width, height, chunk_size=58):
        gcode = ["; jpg begin {}x{} {}".format(width, height, len(encoded_snapshot))]
        chunks = ["; {}".format(encoded_snapshot[i:i + chunk_size]) for i in range(0, len(encoded_snapshot), chunk_size)]
        gcode.extend(chunks)
        gcode.append("; jpg end")
        gcode.append(";")
        return gcode

    # Get the time value from a line as a float.
    def getTimeValue(self, line):
        list_split = re.split(":", line)
        return float(list_split[1])

    def getSettingDataString(self):
        return """{
            "name": "E3S1PROFORKBYTT Thumbnail",
            "key": "E3S1PROFORKBYTT_printdata_crealityslicer_thumbnail",
            "metadata": {},
            "version": 2,
            "settings": {
                "width": {
                    "label": "Width",
                    "description": "Width of the generated thumbnail",
                    "unit": "px",
                    "type": "int",
                    "default_value": 250,
                    "minimum_value": "250",
                    "maximum_value_warning": "250"
                },
                "height": {
                    "label": "Height",
                    "description": "Height of the generated thumbnail",
                    "unit": "px",
                    "type": "int",
                    "default_value": 250,
                    "minimum_value": "250",
                    "maximum_value_warning": "250"
                },
                "Diameter": {
                    "label": "Filament Diameter",
                    "description": "Diameter of the Used Filament",
                    "unit": "mm",
                    "type": "float",
                    "default_value": 1.75,
                    "minimum_value": "1.75",
                    "maximum_value_warning": "3.00"
                },
                "Density": {
                    "label": "Filament Density",
                    "description": "PLA/PETG=1.25, ABS/ASA=1.10",
                    "unit": "g/cm³",
                    "type": "float",
                    "default_value": 1.25,
                    "minimum_value": "1.10",
                    "maximum_value_warning": "2.00"
                }
            }
        }"""


    def execute(self, data):
        try:
            width = self.getSettingValueByKey("width")
            height = self.getSettingValueByKey("height")
            diameter = self.getSettingValueByKey("Diameter")
            diameter_cm = diameter / 10  # Convert mm to cm
            density = self.getSettingValueByKey("Density")
            snapshot = self._createSnapshot(width, height)

            if snapshot:
                encoded_snapshot = self._encodeSnapshot(snapshot)
                snapshot_gcode = self._convertSnapshotToGcode(encoded_snapshot, width, height)
                layer_height_value = 0.0
                filament_used_g = 0.0
                filament_used_m = 0.0
                layers = 0
                total_time = -1

                for layer_index, layer_data in enumerate(data):
                    lines = layer_data.split("\n")
                    for line_index, line in enumerate(lines):
                        if line.startswith(";LAYER:"):
                            layer_number = int(line.split(":")[1]) + 1
                        elif line.startswith(";Filament used:"):
                            filament_used_m = float(line.split(":")[1].split('m')[0].strip())
                            filament_used_cm = filament_used_m * 100
                            filament_used_m = math.ceil(filament_used_m) if filament_used_m > 0 else 0
                            volume_cm3 = math.pi * (diameter_cm / 2) ** 2 * filament_used_cm
                            filament_used_g = math.ceil(volume_cm3 * density) if volume_cm3 * density > 0 else 0
                        elif line.startswith(";Layer height:"):
                            layer_height_value = round(float(line.split(":")[1].strip()), 2)
                        elif line.startswith(";MAXZ:"):
                            maxz_value = round(float(line.split(":")[1].strip()), 2)
                            layers = int(maxz_value / layer_height_value)
                        elif line.startswith(";TIME:") and total_time == -1:
                            total_time = self.getTimeValue(line)

                    data[layer_index] = "\n".join(lines)

                # Insert the snapshot thumbnail G-code
                flavor_line_index = None
                for layer_index, layer_data in enumerate(data):
                    lines = layer_data.split("\n")
                    for line_index, line in enumerate(lines):
                        if line.startswith(";FLAVOR:Marlin"):
                            flavor_line_index = line_index
                            break
                    if flavor_line_index is not None:
                        break

                if flavor_line_index is not None:
                    lines_to_insert = snapshot_gcode + [""]
                    lines = lines[:flavor_line_index] + lines_to_insert + lines[flavor_line_index:]
                    modified_layer_data = "\n".join(lines)
                    data[layer_index] = modified_layer_data

                # Calculate total lines so far for the snapshot
                total_lines_so_far = 0
                for index, layer in enumerate(data):
                    lines = layer.split('\n')
                    for line_index, line in enumerate(lines):
                        if line.startswith("; jpg begin"):
                            start_line_number = total_lines_so_far + line_index + 1
                        if line.startswith("; jpg end"):
                            end_line_number = total_lines_so_far + line_index + 1
                    total_lines_so_far += len(lines)

                # Update the snapshot G-code with total lines and other information
                for index, layer in enumerate(data):
                    lines = layer.split('\n')
                    for line_index, line in enumerate(lines):
                        if line.startswith("; jpg begin"):
                            updated_line = "; jpg begin {}x{} {} {} {} {} {} {} {} {} {}".format(
                                width, height, len(encoded_snapshot), start_line_number, end_line_number,
                                filament_used_m, filament_used_g, layer_height_value, diameter, density, layers)
                            lines[line_index] = updated_line
                    data[index] = "\n".join(lines)

                # Additional time and percentage calculations
                if total_time != -1:
                    filament_used_m_per_layer = filament_used_m / max(layers, 1)  # Avoid division by zero
                    remaining_filament_m = filament_used_m
                    filament_used_g_per_layer = filament_used_g / max(layers, 1)  # Avoid division by zero
                    remaining_filament_g = filament_used_g

                    m117_added_1 = False  # Flag to check if M117 and M73 commands were added for Layer 0
                    for index, layer_data in enumerate(data):
                        lines = layer_data.split("\n")
                        for line_index, line in enumerate(lines):
                            if line.startswith(";LAYER:"):
                                layer_number = int(line.split(":")[1]) + 1
                                # Check if this is Layer 1 and M117/M73 commands have not been added yet
                                if layer_number == 1 and not m117_added_1:
                                    for sub_line_index, sub_line in enumerate(lines):
                                        if sub_line.startswith("G0 ") and "Z{}".format(layer_height_value) in sub_line:
                                            m117_line = "M117 L{} M{} G{} Z{} Q{}".format(layer_number, math.ceil(remaining_filament_m), math.ceil(remaining_filament_g), layer_height_value, layers)
                                            m73_line = "M73 P{} R{}".format(0, int(total_time * (1 - layer_number / layers) / 60))
                                            lines.insert(sub_line_index + 1, m117_line)
                                            lines.insert(sub_line_index + 2, m73_line)
                                            m117_added_1 = True  # Set the flag to True after adding M117 and M73 commands for Layer 0
                                            break
                                # For all other layers, including Layer 1 if M117/M73 commands have not been added
                                if layer_number != 1 and not line.startswith("M117") and not line.startswith("M73"):
                                    m117_line = "M117 L{} M{} G{}".format(layer_number, math.ceil(remaining_filament_m), math.ceil(remaining_filament_g))
                                    m73_line = "M73 P{} R{}".format(int((layer_number / layers) * 100), int(total_time * (1 - layer_number / layers) / 60))
                                    lines.insert(line_index + 1, m117_line)
                                    lines.insert(line_index + 2, m73_line)
                                    break  # Add the commands once and then break out of the loop
                                      
                        data[index] = "\n".join(lines)

                    if not m117_added:
                        Logger.log("w", "No M117 and M73 commands were added for Layer 0. Check the G-code for ';LAYER:' markers.")
                    else:
                        Logger.log("d", "Added M117 and M73 commands for Layer 0 and subsequent layers.")

            else:
                Logger.log("w", "Snapshot not created. Skipping M117 command insertion.")

        except Exception as e:
            Logger.logException("e", "Error in script execution: {}".format(str(e)))

        return data