#!/usr/bin/env python3
#
# Superslicer Slicer remove headers before jpg.
#
# It also adds the needed printdata to show on the main during print.
#
# This script has been developed for E3S1PROFORKBYTT by Thomas Toka.
#
# Intruduced with v008 into E3S1PROFORKBYTT. Extended in v023
# ------------------------------------------------------------------------------

import sys
import os
import math
import base64
from PIL import Image
from io import BytesIO
import re

# Get the g-code source file name
sourceFile = sys.argv[1]

# Read the ENTIRE g-code file into memory
with open(sourceFile, "r", encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
remove_next_line = False

for line in lines:
    if remove_next_line and line.strip() == ';':
        remove_next_line = False
        continue
    if line.startswith('; generated by SuperSlicer'):
        remove_next_line = True
    elif remove_next_line and line.strip() == '':
        continue
    else:
        new_lines.append(line)

# Extract additional information (moved from PrusaSlicer script)
filament_used_m, filament_used_g, filament_diameter, filament_density, layer_height, layers = "0", "0", "0", "0", "0", "0"
for line in new_lines:
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
        layer_height = "{:.2f}".format(round(float(layer_height), 2))
    elif line.startswith("; total layers count ="):
        layers = line.split("=")[1].strip()
    elif line.startswith("; estimated printing time (normal mode) ="):
        time_parts = line.split("=")[1].strip().split()
        days, hours, minutes, seconds = 0, 0, 0, 0
        for part in time_parts:
            if part.endswith('d'):
                days = int(part[:-1])
            elif part.endswith('h'):
                hours = int(part[:-1])
            elif part.endswith('m'):
                minutes = int(part[:-1])
            elif part.endswith('s'):
                seconds = int(part[:-1])
        total_time_minutes = (days * 24 * 60) + (hours * 60) + minutes + (seconds / 60)

layers = int(layers)
filament_used_m_per_layer = filament_used_m / max(layers, 1)  # Avoid division by zero
remaining_filament_m = filament_used_m

filament_used_g_per_layer = filament_used_g / max(layers, 1)  # Avoid division by zero
remaining_filament_g = filament_used_g

m117_added = 0  # Counter for added M117 commands
first_layer = True

# Find the existing thumbnail header and footer lines
thumbnail_start = None
thumbnail_end = None

for i, line in enumerate(new_lines):
    if line.startswith('; thumbnail_JPG begin'):
        thumbnail_start = i
    elif line.startswith('; thumbnail_JPG end'):
        thumbnail_end = i

if thumbnail_start is not None and thumbnail_end is not None:
    # Extract the PNG data without decoding
    original_png_data = "".join(new_lines[thumbnail_start + 1:thumbnail_end]).replace("; ", "")

    # Define a maximum line length for the PNG data
    max_line_length = 75 - len("; ")

    # Split the PNG data into lines with a maximum length
    num_lines = 0
    while original_png_data:
        if len(original_png_data) <= max_line_length:
            line = original_png_data
            original_png_data = ""
        else:
            line = original_png_data[:max_line_length]
            original_png_data = original_png_data[max_line_length:]

        # Add the line to the list of lines
        lines.append(line)
        num_lines += 1

    # Calculate the number of lines in the thumbnail data
    # (this was already done but not used)
    num_lines = len(lines)

    # Replace the old PNG lines with the new PNG lines
    new_lines[thumbnail_start + 1:thumbnail_end] = [line + "\n" for line in lines]

    # Update the '; thumbnail_JPG begin' line
    start_line_number = 1
    end_line_number = start_line_number + num_lines
    new_lines[thumbnail_start] = (
        f"; thumbnail_JPG begin 250x250 {len(''.join(lines))} {start_line_number} {end_line_number}"
        f" {filament_used_m} {filament_used_g} {layer_height} {filament_diameter} {filament_density} {layers}\n"
    )

# Find the ';AFTER_LAYER_CHANGE' line and add 'M117' after it
for i, line in enumerate(new_lines):
    if line.strip() == ';AFTER_LAYER_CHANGE':
        if first_layer:
            m117_line = "M117 L1 M{} G{} Z{} Q{}".format(math.ceil(remaining_filament_m), math.ceil(remaining_filament_g), layers, layer_height)
            new_lines.insert(i + 1, m117_line + '\n')
            m73_line_r = "M73 R{}".format(int(total_time_minutes * (1 - m117_added / layers)))
            new_lines.insert(i + 2, m73_line_r + '\n')
            m73_line_p = "M73 P{}".format(int((m117_added / layers) * 100))
            new_lines.insert(i + 3, m73_line_p + '\n')
            first_layer = False
        else:
            m117_line = "M117 L{} M{} G{}".format(m117_added + 1, math.ceil(remaining_filament_m), math.ceil(remaining_filament_g))
            new_lines.insert(i + 1, m117_line + '\n')
            if m117_added == layers - 1:
                m73_line_r = "M73 R{}".format(int(total_time_minutes * (1 - m117_added / layers)))
                new_lines.insert(i + 2, m73_line_r + '\n')
                m73_line_p = "M73 P{}".format(100)
                new_lines.insert(i + 3, m73_line_p + '\n')
            else:
                m73_line_r = "M73 R{}".format(int(total_time_minutes * (1 - m117_added / layers)))
                new_lines.insert(i + 2, m73_line_r + '\n')
                m73_line_p = "M73 P{}".format(int((m117_added / layers) * 100))
                new_lines.insert(i + 3, m73_line_p + '\n')
            new_lines.insert(i + 2, m73_line + '\n')
        remaining_filament_m -= filament_used_m_per_layer
        remaining_filament_g -= filament_used_g_per_layer
        m117_added += 1

# Write the modified content back to the original file
with open(sourceFile, "w", encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"Added {m117_added} M117 commands and M73 with time information.")