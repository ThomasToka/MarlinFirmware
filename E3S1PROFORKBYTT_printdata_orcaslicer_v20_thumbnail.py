#!/usr/bin/env python3
#
# Orca Slicer as of v20 remove headers before jpg and convert PNG to JPG.
#
# This script has been developed for E3S1PROFORKBYTT by Thomas Toka.
#
# ------------------------------------------------------------------------------

import sys
import base64
import math
from PIL import Image
from io import BytesIO
import os
import platform

if platform.system() == "Darwin":
    print("Running on macOS")
    script_directory = os.path.dirname(os.path.abspath(__file__))
    source_file = sys.argv[1]
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

    # Remove any empty lines and lines that are just a semicolon
    lines = [line for line in lines if line.strip() and not line == ';\n']

    # Extract additional information
    filament_used_m, filament_used_g, filament_diameter, filament_density, layer_height = "0", "0", "0", "0", "0"
    layers = 0
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
        elif line.startswith(";AFTER_LAYER_CHANGE"):
            layers += 1

    filament_used_m_per_layer = filament_used_m / max(layers, 1)  # Avoid division by zero
    remaining_filament_m = filament_used_m

    filament_used_g_per_layer = filament_used_g / max(layers, 1)  # Avoid division by zero
    remaining_filament_g = filament_used_g

    m117_added = 0  # Counter for added M117 commands

    # Counting AFTER_LAYER_CHANGE occurrences
    after_layer_change_count = sum(';AFTER_LAYER_CHANGE' in line for line in lines) - 1

    # Find the thumbnail start and end lines
    thumbnail_start, thumbnail_end = None, None
    for i, line in enumerate(lines):
        if '; thumbnail begin' in line:
            thumbnail_start = i
        elif '; thumbnail end' in line:
            thumbnail_end = i
            break

    if thumbnail_start is not None and thumbnail_end is not None:
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
        max_line_length = 79 - len("; ")
        injected_jpg_data = ["; " + image_jpg_base64[i:i + max_line_length] for i in range(0, len(image_jpg_base64), max_line_length)]

        lines = lines[thumbnail_start:]

        # Replace the old PNG lines with the new JPEG lines
        lines[1:thumbnail_end - thumbnail_start] = [line + "\n" for line in injected_jpg_data]

        # Update the '; thumbnail_JPG begin' line using 'after_layer_change_count'
        start_line_number = 1
        end_line_number = start_line_number + len(injected_jpg_data) + 1
        lines[0] = f'; thumbnail_JPG begin 250x250 {len(image_jpg_data)} {start_line_number} {end_line_number} {filament_used_m} {filament_used_g} {layer_height} {filament_diameter} {filament_density} {after_layer_change_count}\n'

    # Insert 'M117 Pxxx Qxxx' before each ';AFTER_LAYER_CHANGE'
    layer_number = 0

    for i in range(len(lines)):
        if lines[i].startswith(';AFTER_LAYER_CHANGE'):
            z_value_line = lines[i + 1].strip()
            
            # Look for a part that appears to be a Z value and remove leading semicolons
            z_value_parts = next((part for part in [z_value_line.lstrip(';')] if part.replace('.', '', 1).isdigit()), None)
            
            if z_value_parts:
                z_value = z_value_parts
                if z_value.startswith('0'):
                    z_value = z_value.lstrip('0')
                # Search for the corresponding G1 Z line within a range of lines
                found_g1_z = False
                j = i + 2  # Start searching from the line after ';AFTER_LAYER_CHANGE'
                max_search_lines = 20  # Adjust this value as needed
                
                while j < min(len(lines), i + max_search_lines):
                    line = lines[j].strip()
                    if 'G1' in line and f'Z{z_value}' in line:
                        found_g1_z = True
                        break
                    j += 1

                if found_g1_z:
                    if layer_number == 0:
                        m117_line = "M117 L1 M{} G{} Z{} Q{}".format(math.ceil(remaining_filament_m), math.ceil(remaining_filament_g), layers, layer_height)
                    else:
                        m117_line = "M117 L{} M{} G{}".format(layer_number + 1, math.ceil(remaining_filament_m), math.ceil(remaining_filament_g))
                    lines.insert(j + 1, m117_line + '\n')
                    remaining_filament_m -= filament_used_m_per_layer
                    remaining_filament_g -= filament_used_g_per_layer
                    m117_added += 1  # Increment counter
                    layer_number += 1
                else:
                    print(f"Warning: No matching G1 Z line found for Z{z_value} after ';AFTER_LAYER_CHANGE'.")
            else:
                print(f"Warning: No Z value found after ';AFTER_LAYER_CHANGE'.")

    with open(source_file, "w", encoding='utf-8') as f:
        f.writelines(lines)

    print(f"Added {m117_added} M117 commands.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 E3S1PROFORKBYTT_printdata_orcaslicer_v20_thumbnail.py <input.gcode>")
        sys.exit(1)

    if platform.system() == "Darwin":
        main(source_file)
    else:
        main(sys.argv[1])
