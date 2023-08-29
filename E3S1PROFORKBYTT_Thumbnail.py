#------------------------------------------------------------------------------
# Cura 5.4 JPEG Thumbnail creator
#
# This script has been changed for E3S1PROFORKBYTT by Thomas Toka.
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

from UM.Logger import Logger
from cura.Snapshot import Snapshot
from cura.CuraVersion import CuraVersion

from ..Script import Script


class E3S1PROFORKBYTT_Thumbnail(Script):
    def __init__(self):
        super().__init__()

    def _createSnapshot(self, width, height):
        Logger.log("d", "Creating thumbnail image...")
        try:
            return Snapshot.snapshot(width, height)
        except Exception:
            Logger.logException("w", "Failed to create snapshot image")

    def _encodeSnapshot(self, snapshot):

        Major=0
        Minor=0
        try:
          Major = int(CuraVersion.split(".")[0])
          Minor = int(CuraVersion.split(".")[1])
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
            thumbnail_image = snapshot
            thumbnail_image.save(thumbnail_buffer, "JPG")
            base64_bytes = base64.b64encode(thumbnail_buffer.data())
            base64_message = base64_bytes.decode('ascii')
            thumbnail_buffer.close()
            return base64_message
        except Exception:
            Logger.logException("w", "Failed to encode snapshot image")

    def _convertSnapshotToGcode(self, encoded_snapshot, width, height, chunk_size=58):
        gcode = []

        encoded_snapshot_length = len(encoded_snapshot)
        gcode.append("; jpg begin {}x{} {}".format(
            width, height, encoded_snapshot_length))

        chunks = ["; {}".format(encoded_snapshot[i:i+chunk_size])
                  for i in range(0, len(encoded_snapshot), chunk_size)]
        gcode.extend(chunks)

        gcode.append("; jpg end")
        gcode.append(";")

        return gcode

    def getSettingDataString(self):
        return """{
            "name": "E3S1PROFORKBYTT Thumbnail",
            "key": "E3S1PROFORKBYTT_Thumbnail",
            "metadata": {},
            "version": 2,
            "settings":
            {
                "width":
                {
                    "label": "Width",
                    "description": "Width of the generated thumbnail",
                    "unit": "px",
                    "type": "int",
                    "default_value": 200,
                    "minimum_value": "200",
                    "minimum_value_warning": "200",
                    "maximum_value_warning": "200"
                },
                "height":
                {
                    "label": "Height",
                    "description": "Height of the generated thumbnail",
                    "unit": "px",
                    "type": "int",
                    "default_value": 200,
                    "minimum_value": "200",
                    "minimum_value_warning": "200",
                    "maximum_value_warning": "200"
                }
            }
        }"""

    def execute(self, data):
        width = self.getSettingValueByKey("width")
        height = self.getSettingValueByKey("height")

        snapshot = self._createSnapshot(width, height)
        if snapshot:
            encoded_snapshot = self._encodeSnapshot(snapshot)
            snapshot_gcode = self._convertSnapshotToGcode(
                encoded_snapshot, width, height)

            # Find the index of the line starting with ;FLAVOR:Marlin
            flavor_line_index = None
            for layer_data in data:
                lines = layer_data.split("\n")
                for line in lines:
                    if line.startswith(";FLAVOR:Marlin"):
                        flavor_line_index = lines.index(line)
                        break
                if flavor_line_index is not None:
                    break

            # Insert snapshot_gcode before ;FLAVOR:Marlin
            if flavor_line_index is not None:
                lines_to_insert = snapshot_gcode + [""]  # Add a blank line after snapshot_gcode
                lines[flavor_line_index:flavor_line_index] = lines_to_insert

                # Join the modified lines for this layer
                modified_layer_data = "\n".join(lines)
                data[data.index(layer_data)] = modified_layer_data

        return data
