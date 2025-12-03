#!/usr/bin/env python3
#
# BambuStudio thumbnail PNG → JPG converter.
# - Preserves all original content (except the old thumbnail block).
# - Converts the original embedded PNG thumbnail (e.g. 50x50) to a 250x250 JPG.
# - Scales the original image up and centers it in a 250x250 canvas.
# - Inserts the JPG thumbnail block at the very top of the file.
# - Removes the original thumbnail block entirely.
# - adds printdate for the E3S1PROFORKBYTT eco system
# Developed for E3S1PROFORKBYTT by Thomas Toka.
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
    # Read the entire G-code file into memory (preserve all lines as-is)
    with open(source_file, "r", encoding='utf-8') as f:
        lines = f.readlines()

    # Extract additional information
    filament_used_m, filament_used_g = 0.0, 0.0
    filament_diameter, filament_density, layer_height = "0", "0", "0"
    header_layers = None
    marker_layers = 0

    # --- First pass: parse metadata & count layers --------------------------------
    for line in lines:
        stripped = line.strip()

        # --- Orca-style fields -------------------------------------------------
        if stripped.startswith("; filament used [mm] ="):
            filament_used_mm_values = [
                float(value.strip())
                for value in stripped.split("=", 1)[1].strip().split(',')
            ]
            filament_used_m_val = sum(filament_used_mm_values) / 1000.0  # mm → m
            filament_used_m = math.ceil(filament_used_m_val) if filament_used_m_val > 0 else 0

        elif stripped.startswith("; filament used [g] ="):
            filament_used_g_values = [
                float(value.strip())
                for value in stripped.split("=", 1)[1].strip().split(',')
            ]
            filament_used_g_val = sum(filament_used_g_values)
            filament_used_g = math.ceil(filament_used_g_val) if filament_used_g_val > 0 else 0

        elif stripped.startswith("; filament_diameter ="):
            filament_diameter_values = [
                float(value.strip())
                for value in stripped.split("=", 1)[1].strip().split(',')
            ]
            fd = round(sum(filament_diameter_values) / len(filament_diameter_values), 2)
            filament_diameter = f"{fd:.2f}"

        elif stripped.startswith("; filament_density ="):
            filament_density_values = [
                float(value.strip())
                for value in stripped.split("=", 1)[1].strip().split(',')
            ]
            fdens = round(sum(filament_density_values) / len(filament_density_values), 2)
            filament_density = f"{fdens:.2f}"

        elif stripped.startswith("; layer_height ="):
            layer_height_values = [
                float(value.strip())
                for value in stripped.split("=", 1)[1].strip().split(',')
            ]
            lh = round(sum(layer_height_values) / len(layer_height_values), 2)
            layer_height = f"{lh:.2f}"

        # --- BambuStudio-style fields -----------------------------------------
        elif stripped.startswith("; total filament length [mm]"):
            # Example: ; total filament length [mm] : 2585.91
            try:
                val_str = stripped.split(":", 1)[1].strip()
                filament_used_mm = float(val_str)
                filament_used_m_val = filament_used_mm / 1000.0
                filament_used_m = math.ceil(filament_used_m_val) if filament_used_m_val > 0 else 0
            except Exception:
                pass

        elif stripped.startswith("; total filament weight [g]"):
            # Example: ; total filament weight [g] : 7.71
            try:
                val_str = stripped.split(":", 1)[1].strip()
                filament_used_g_val = float(val_str)
                filament_used_g = math.ceil(filament_used_g_val) if filament_used_g_val > 0 else 0
            except Exception:
                pass

        elif stripped.startswith("; filament_diameter:"):
            # Example: ; filament_diameter: 1.75
            try:
                val_str = stripped.split(":", 1)[1].strip()
                fd = float(val_str)
                filament_diameter = f"{fd:.2f}"
            except Exception:
                pass

        elif stripped.startswith("; filament_density:"):
            # Example: ; filament_density: 1.24
            try:
                val_str = stripped.split(":", 1)[1].strip()
                fdens = float(val_str)
                filament_density = f"{fdens:.2f}"
            except Exception:
                pass

        elif stripped.startswith("; total layer number:"):
            # Example: ; total layer number: 75
            try:
                val_str = stripped.split(":", 1)[1].strip()
                header_layers = int(float(val_str))
            except Exception:
                pass

        # --- Layer markers -----------------------------------------------------
        elif stripped.startswith(";AFTER_LAYER_CHANGE"):
            marker_layers += 1

    # Decide final layer count: prefer header, fallback to markers
    if header_layers is not None:
        layers = header_layers
    else:
        layers = marker_layers

    # Avoid division by zero
    layers_for_average = max(layers, 1)
    filament_used_m_per_layer = filament_used_m / layers_for_average
    filament_used_g_per_layer = filament_used_g / layers_for_average
    remaining_filament_m = filament_used_m
    remaining_filament_g = filament_used_g

    m117_added = 0  # Counter for added M117 commands

    # Counting AFTER_LAYER_CHANGE occurrences for thumbnail metadata
    after_layer_change_count = sum(';AFTER_LAYER_CHANGE' in line for line in lines) - 1
    if after_layer_change_count < 0:
        after_layer_change_count = 0

    # --- Find thumbnail block (PNG) -------------------------------------------
    thumbnail_start, thumbnail_end = None, None
    block_start, block_end = None, None

    for i, line in enumerate(lines):
        if '; THUMBNAIL_BLOCK_START' in line and block_start is None:
            block_start = i
        if '; thumbnail begin' in line and thumbnail_start is None:
            thumbnail_start = i
        if '; thumbnail end' in line:
            thumbnail_end = i
        if '; THUMBNAIL_BLOCK_END' in line:
            block_end = i

    # Fallback if there is no THUMBNAIL_BLOCK wrapper
    if thumbnail_start is not None and thumbnail_end is not None:
        if block_start is None:
            block_start = thumbnail_start
        if block_end is None:
            block_end = thumbnail_end

        # Extract and decode the PNG data from between thumbnail begin/end
        original_png_data = "".join(
            l.replace("; ", "")
            for l in lines[thumbnail_start + 1:thumbnail_end]
        )
        png_data_bytes = base64.b64decode(original_png_data)

        # Load original thumbnail (e.g. 50x50 from BambuStudio)
        original = Image.open(BytesIO(png_data_bytes)).convert("RGB")

        # --- Create a 250x250 canvas and center a scaled version of original ---
        target_size = 250
        # Scale up original to 250x250 (keeps aspect ratio; for square images it's exact)
        scaled = original.resize((target_size, target_size), Image.LANCZOS)

        canvas = Image.new("RGB", (target_size, target_size), (255, 255, 255))
        x = (target_size - scaled.width) // 2  # will be 0 for 1:1 aspect
        y = (target_size - scaled.height) // 2
        canvas.paste(scaled, (x, y))

        # Encode the 250×250 JPG
        buffer = BytesIO()
        canvas.save(buffer, format="JPEG")
        image_jpg_data = buffer.getvalue()

        # Base64 encode the JPEG data
        image_jpg_base64 = base64.b64encode(image_jpg_data).decode('utf-8')

        # Split the base64 string into formatted lines
        max_line_length = 79 - len("; ")
        injected_jpg_data = [
            "; " + image_jpg_base64[i:i + max_line_length]
            for i in range(0, len(image_jpg_base64), max_line_length)
        ]

        # Build the new JPG thumbnail block that will go at the very top
        start_line_number = 1
        end_line_number = start_line_number + len(injected_jpg_data) + 1

        new_thumb_block = []
        new_thumb_block.append(
            f'; thumbnail_JPG begin 250x250 {len(image_jpg_data)} '
            f'{start_line_number} {end_line_number} '
            f'{filament_used_m} {filament_used_g} {layer_height} '
            f'{filament_diameter} {filament_density} {after_layer_change_count}\n'
        )
        new_thumb_block.extend([l + "\n" for l in injected_jpg_data])
        new_thumb_block.append("; thumbnail end\n")

        # Remove the original thumbnail block entirely
        # (including THUMBNAIL_BLOCK_START/END if present)
        content_without_old_thumb = lines[:block_start] + lines[block_end + 1:]

        # Prepend the new JPG thumbnail block as the first content
        lines = new_thumb_block + content_without_old_thumb

    # --- Insert 'M117 ...' after each layer change ----------------------------
    layer_number = 0

    i = 0
    while i < len(lines):
        if lines[i].startswith(';AFTER_LAYER_CHANGE'):
            z_value_line = lines[i + 1].strip() if i + 1 < len(lines) else ""

            # Look for a part that appears to be a Z value and remove leading semicolons
            z_value_parts = next(
                (part for part in [z_value_line.lstrip(';')]
                 if part.replace('.', '', 1).isdigit()),
                None
            )

            if z_value_parts:
                z_value = z_value_parts
                if z_value.startswith('0') and z_value != "0":
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
                        m117_line = "M117 L1 M{} G{} Z{} Q{}".format(
                            math.ceil(remaining_filament_m),
                            math.ceil(remaining_filament_g),
                            layers,
                            layer_height
                        )
                    else:
                        m117_line = "M117 L{} M{} G{}".format(
                            layer_number + 1,
                            math.ceil(remaining_filament_m),
                            math.ceil(remaining_filament_g)
                        )
                    lines.insert(j + 1, m117_line + '\n')
                    remaining_filament_m -= filament_used_m_per_layer
                    remaining_filament_g -= filament_used_g_per_layer
                    m117_added += 1  # Increment counter
                    layer_number += 1
                    i = j + 2  # Skip past the inserted line
                    continue
                else:
                    print(
                        f"Warning: No matching G1 Z line found for Z{z_value} "
                        f"after ';AFTER_LAYER_CHANGE'."
                    )
            else:
                print("Warning: No Z value found after ';AFTER_LAYER_CHANGE'.")
        i += 1

    with open(source_file, "w", encoding='utf-8') as f:
        f.writelines(lines)

    print(f"Added {m117_added} M117 commands.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 E3S1PROFORKBYTT_printdata_bambustudio_thumbnail.py <input.gcode>")
        sys.exit(1)

    if platform.system() == "Darwin":
        main(source_file)
    else:
        main(sys.argv[1])
