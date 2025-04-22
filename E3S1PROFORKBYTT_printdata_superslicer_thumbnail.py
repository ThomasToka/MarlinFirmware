#!/usr/bin/env python3
#
# Superslicer Slicer remove headers before jpg.
#
# It also adds the needed printdata to show on the main during print.
#
# This script has been developed for E3S1PROFORKBYTT by Thomas Toka.
#
# Introduced with v008 into E3S1PROFORKBYTT. Extended in v023
# ------------------------------------------------------------------------------

import sys
import math

sourceFile = sys.argv[1]

with open(sourceFile, "r", encoding='utf-8') as f:
    lines = f.readlines()

thumbnail_start, thumbnail_end = None, None
for i, line in enumerate(lines):
    if line.startswith('; thumbnail begin') and thumbnail_start is None:
        thumbnail_start = i
    elif line.startswith('; thumbnail end') and thumbnail_start is not None:
        thumbnail_end = i
        break

# Remove original thumbnail completely if exists
if thumbnail_start is not None and thumbnail_end is not None:
    original_jpeg_data = "".join(lines[thumbnail_start + 1:thumbnail_end]).replace("; ", "").replace("\n", "")
    del lines[thumbnail_start:thumbnail_end + 1]
else:
    original_jpeg_data = ""

# Extract additional info
filament_used_m, filament_used_g, filament_diameter, filament_density, layer_height, layers, total_time_minutes = 0, 0, 0, 0, 0, 0, 0
for line in lines:
    if line.startswith("; filament used [mm] ="):
        filament_used_m = math.ceil(float(line.split("=")[1].strip()) / 1000)
    elif line.startswith("; filament used [g] ="):
        filament_used_g = math.ceil(float(line.split("=")[1].strip()))
    elif line.startswith("; filament_diameter ="):
        filament_diameter = float(line.split("=")[1].strip())
    elif line.startswith("; filament_density ="):
        filament_density = float(line.split("=")[1].strip())
    elif line.startswith("; layer_height ="):
        layer_height = "{:.2f}".format(float(line.split("=")[1].strip()))
    elif line.startswith("; total layers count ="):
        layers = int(line.split("=")[1].strip())
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
        total_time_minutes = days * 1440 + hours * 60 + minutes + seconds / 60

max_line_length = 75 - len("; ")
jpeg_lines = [original_jpeg_data[i:i + max_line_length] for i in range(0, len(original_jpeg_data), max_line_length)]
num_lines = len(jpeg_lines)

thumbnail_block = [
    f"; thumbnail begin 250x250 {len(original_jpeg_data)} 1 {num_lines} {filament_used_m} {filament_used_g} {layer_height} {filament_diameter} {filament_density} {layers}\n"
] + ["; " + line + "\n" for line in jpeg_lines] + ["; thumbnail end\n"]

lines = thumbnail_block + lines

filament_used_m_per_layer = filament_used_m / max(layers, 1)
filament_used_g_per_layer = filament_used_g / max(layers, 1)
remaining_filament_m = filament_used_m
remaining_filament_g = filament_used_g
m117_added, first_layer = 0, True

for i in range(len(lines)):
    if lines[i].startswith(';AFTER_LAYER_CHANGE'):
        if first_layer:
            m117_line = f"M117 L1 M{int(remaining_filament_m)} G{int(remaining_filament_g)} Z{layers} Q{layer_height}"
            first_layer = False
        else:
            m117_line = f"M117 L{m117_added + 1} M{int(remaining_filament_m)} G{int(remaining_filament_g)}"

        m73_line_r = f"M73 R{int(total_time_minutes * (1 - m117_added / layers))}"
        m73_line_p = f"M73 P{int((m117_added / layers) * 100)}"

        lines.insert(i + 1, m117_line + '\n')
        lines.insert(i + 2, m73_line_r + '\n')
        lines.insert(i + 3, m73_line_p + '\n')

        remaining_filament_m -= filament_used_m_per_layer
        remaining_filament_g -= filament_used_g_per_layer
        m117_added += 1

with open(sourceFile, "w", encoding='utf-8') as f:
    f.writelines(lines)

print(f"Added {m117_added} M117 commands and M73 with time information.")

