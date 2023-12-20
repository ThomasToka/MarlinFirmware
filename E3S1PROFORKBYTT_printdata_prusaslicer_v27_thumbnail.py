#!/usr/bin/env python3
#
# Prusa Slicer as of v2.7 remove headers before jpg and convert PNG to JPG.
#
# This script has been developed for E3S1PROFORKBYTT by Thomas Toka.
#
# ------------------------------------------------------------------------------

import sys
import base64
import math
from PIL import Image
from io import BytesIO

def main(source_file):
    # Read the entire G-code file into memory
    with open(source_file, "r") as f:
        lines = f.readlines()

    # Remove any empty lines and lines that are just a semicolon
    lines = [line for line in lines if line.strip() and not line == ';\n']

    # Extract additional information
    filament_used_m, filament_used_g, filament_diameter, filament_density, layer_height = "0", "0", "0", "0", "0"
    layers = 0
    for line in lines:
        if line.startswith("; filament used [mm] ="):
            filament_used_mm = float(line.split("=")[1].strip())
            filament_used_m = round(filament_used_mm / 1000, 2)
            if filament_used_m > 0:
                filament_used_m = math.ceil(filament_used_m)
            else:
                filament_used_m = 0
        elif line.startswith("; filament used [g] ="):
            filament_used_g = float(line.split("=")[1].strip())
            filament_used_g = round(filament_used_g, 2)
            if filament_used_g > 0:
                filament_used_g = math.ceil(filament_used_g)
            else:
                filament_used_g = 0
        elif line.startswith("; filament_diameter ="):
            filament_diameter = float(line.split("=")[1].strip())
        elif line.startswith("; filament_density ="):
            filament_density = float(line.split("=")[1].strip())
        elif line.startswith("; layer_height ="):
            layer_height = line.split("=")[1].strip()
            layer_height = round(float(layer_height), 2)
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

        # Replace the old PNG lines with the new JPEG lines
        lines[thumbnail_start + 1:thumbnail_end] = [line + "\n" for line in injected_jpg_data]

        # Update the '; thumbnail_JPG begin' line using 'after_layer_change_count'
        start_line_number = 1
        end_line_number = start_line_number + len(injected_jpg_data) + 1
        lines[thumbnail_start] = f'; thumbnail_JPG begin 250x250 {len(image_jpg_data)} {start_line_number} {end_line_number} {filament_used_m} {filament_used_g} {layer_height} {filament_diameter} {filament_density} {after_layer_change_count}\n'

    # Insert 'M117 Pxxx Qxxx' before each ';AFTER_LAYER_CHANGE'
    layer_number = 0
    i = 0
    while i < len(lines):
        if lines[i].startswith(';AFTER_LAYER_CHANGE'):
            if layer_number == 0:
                m117_line = "M117 L1 M{} G{} Z{} Q{}".format(math.ceil(remaining_filament_m), math.ceil(remaining_filament_g), layers, layer_height)
            else:
                m117_line = "M117 L{} M{} G{}".format(layer_number + 1, math.ceil(remaining_filament_m), math.ceil(remaining_filament_g))
            lines.insert(i, m117_line + '\n')
            remaining_filament_m -= filament_used_m_per_layer
            remaining_filament_g -= filament_used_g_per_layer
            m117_added += 1  # Increment counter
            layer_number += 1
            i += 1
        i += 1

    if m117_added > 0:
        print("Added {} M117 commands.".format(m117_added))
    else:
        print("No M117 commands were added. Check the G-code for ';AFTER_LAYER_CHANGE' markers.")

    # Remove the '; generated by PrusaSlicer' line and any leading semicolons or empty lines
    lines = [line for line in lines if line.strip() and not line.startswith('; generated by PrusaSlicer')]

    # Write the modified content back to the original file
    with open(source_file, "w") as f:
        f.writelines(lines)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script.py <gcode-file>")
        sys.exit(1)

    main(sys.argv[1])
