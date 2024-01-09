#!/usr/bin/env python3
#
# Orca Slicer as of v19 remove headers before jpg and convert PNG to JPG.
#
# This script has been developed for E3S1PROFORKBYTT by Thomas Toka.
#
# ------------------------------------------------------------------------------

import sys
import math
import base64
from PIL import Image
from io import BytesIO
import re
import os
import platform

if platform.system() == "Darwin":
    print("Running on macOS")
    script_directory = os.path.dirname(os.path.abspath(__file__))
    source_file  = sys.argv[1]
    source_file = os.path.join(script_directory, source_file)
    if not os.path.exists(source_file):
        print(f"The file '{source_file}' does not exist.")
        sys.exit(1)
    else:
        print(f"The file '{source_file}' exists.")
else:
    print("Not running on macOS")

def main(source_file):
    # Read the entire G-code file into memory
    with open(source_file, "r", encoding='utf-8') as f:
        lines = f.readlines()

    # Extract additional information
    filament_used_m, filament_used_g, filament_diameter, filament_density, layer_height, layers = "0", "0", "0", "0", "0", "0"
    for line in lines:
        if line.startswith("; filament used [mm] ="):
            filament_used_mm_values = [float(value.strip()) for value in line.split("=")[1].strip().split(',')]
            filament_used_m = round(sum(filament_used_mm_values) / 1000, 2)  # Convert mm to meters
            if filament_used_m > 0:
                filament_used_m = math.ceil(filament_used_m)
            else:
                filament_used_m = 0
        elif line.startswith("; filament used [g] ="):
            filament_used_g_values = [float(value.strip()) for value in line.split("=")[1].strip().split(',')]
            filament_used_g = round(sum(filament_used_g_values), 2)
            if filament_used_g > 0:
                filament_used_g = math.ceil(filament_used_g)
            else:
                filament_used_g = 0
        elif line.startswith("; filament_diameter ="):
            filament_diameter_values = [float(value.strip()) for value in line.split("=")[1].strip().split(',')]
            filament_diameter = round(sum(filament_diameter_values) / len(filament_diameter_values), 2)
            filament_diameter = "{:.2f}".format(filament_diameter)
        elif line.startswith("; filament_density ="):
            filament_density_values = [float(value.strip()) for value in line.split("=")[1].strip().split(',')]
            filament_density = round(sum(filament_density_values) / len(filament_density_values), 2)  # Calculate the median
            filament_density = "{:.2f}".format(filament_density)
        elif line.startswith("; layer_height ="):
            layer_height_values = [float(value.strip()) for value in line.split("=")[1].strip().split(',')]
            layer_height = round(sum(layer_height_values) / len(layer_height_values), 2)  # Calculate the median
            layer_height = "{:.2f}".format(layer_height)
        elif line.startswith("; total layers count ="):
            layers = line.split("=")[1].strip()

    layers = int(layers)
    filament_used_m_per_layer = filament_used_m / max(layers, 1)  # Avoid division by zero
    remaining_filament_m = filament_used_m

    filament_used_g_per_layer = filament_used_g / max(layers, 1)  # Avoid division by zero
    remaining_filament_g = filament_used_g

    m117_added = 0  # Counter for added M117 commands

    # Convert the thumbnail from PNG to JPEG
    thumbnail_start = None
    for i, line in enumerate(lines):
        if '; thumbnail begin' in line:
            thumbnail_start = i
            break

    if thumbnail_start is not None:
        # Find the thumbnail end line
        thumbnail_end = next((i for i, line in enumerate(lines[thumbnail_start:], start=thumbnail_start) if '; thumbnail end' in line), None)

        if thumbnail_end is not None:
            # Extract and decode the PNG data
            original_png_data = "".join(lines[thumbnail_start + 1:thumbnail_end]).replace("; ", "")
            png_data_bytes = base64.b64decode(original_png_data)
            image = Image.open(BytesIO(png_data_bytes))
            image = image.convert("RGB")

            # Encode the image as JPEG
            buffer = BytesIO()
            image.save(buffer, format="JPEG")
            image_jpg_data = buffer.getvalue()

            # Base64 encode the JPEG data
            image_jpg_base64 = base64.b64encode(image_jpg_data).decode('utf-8')

            # Split the base64 string into formatted lines
            max_line_length = 74 - len("; ")
            injected_jpg_data = ["; " + image_jpg_base64[i:i + max_line_length] for i in range(0, len(image_jpg_base64), max_line_length)]

            # Remove everything before the '; thumbnail_JPG begin' line
            lines = lines[thumbnail_start:]

            # Replace the old PNG lines with the new JPEG lines
            lines[1:thumbnail_end - thumbnail_start] = [line + "\n" for line in injected_jpg_data]

            # Update start and end line numbers
            start_line_number = 1  # The line immediately after '; thumbnail_JPG begin'
            end_line_number = start_line_number + len(injected_jpg_data) + 1

            # Update the '; thumbnail_JPG begin' line
            lines[0] = f'; thumbnail_JPG begin 250x250 {len(image_jpg_data)} {start_line_number} {end_line_number} {filament_used_m} {filament_used_g} {layer_height} {filament_diameter} {filament_density} {layers}\n'

    # Find the ';LAYER_CHANGE' line and add 'M117' after the next 'G1 Z' line with the corresponding 'Z' value
    layer_number = 0
    layer_change_found = False
    for i in range(len(lines)):
        if lines[i].strip() == ";LAYER_CHANGE":
            layer_number += 1
            layer_change_found = True
        elif layer_change_found:
            match = re.search(r";Z:([\d.]+)", lines[i])
            if match:
                z_value = match.group(1)  # Extract the Z value
                next_g1_z_index = i + 1
                while next_g1_z_index < len(lines):
                    if float(z_value) >= 1:
                        g1_z_regex = fr"G1 Z{z_value}(?=\s|$)"
                    else:
                        # Adjust regex for Z values less than 1
                        simplified_z_value = z_value.lstrip('0').rstrip('0').rstrip('.')
                        if '.' in z_value and not simplified_z_value.startswith('.'):
                            simplified_z_value = '.' + simplified_z_value
                        g1_z_regex = fr"G1 Z{simplified_z_value}(?=\s|$)"
                    if re.search(g1_z_regex, lines[next_g1_z_index]):
                        if layer_number == 1:
                            m117_line = "M117 L1 M{} G{} Z{} Q{}".format(math.ceil(remaining_filament_m), math.ceil(remaining_filament_g), layers, layer_height)
                        else:
                            m117_line = "M117 L{} M{} G{}".format(layer_number, math.ceil(remaining_filament_m), math.ceil(remaining_filament_g))
                        lines.insert(next_g1_z_index + 1, m117_line + '\n')
                        remaining_filament_m -= filament_used_m_per_layer
                        remaining_filament_g -= filament_used_g_per_layer
                        m117_added += 1
                        break
                    next_g1_z_index += 1

    # Add M117 for the very first layer
    if m117_added == 0:
        m117_line = "M117 L1 M{} G{} Z{} Q{}".format(math.ceil(remaining_filament_m), math.ceil(remaining_filament_g), layers, layer_height)
        lines.insert(0, m117_line + '\n')

    # Write the modified content back to the original file
    with open(source_file, "w", encoding='utf-8') as f:
        f.writelines(lines)

    print(f"Added {m117_added + 1} M117 commands.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script.py <gcode-file>")
        sys.exit(1)
    if platform.system() == "Darwin":
        main(source_file)
    else:
        main(sys.argv[1])
