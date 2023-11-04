#!/usr/bin/env python3
#
# Orca Slicer remove headers before jpg and convert PNG to JPG.
#
# This script has been developed for E3S1PROFORKBYTT by Thomas Toka.
#
# ------------------------------------------------------------------------------

import sys
import base64
from PIL import Image
from io import BytesIO

def main(source_file):
    # Read the ENTIRE g-code file into memory
    with open(source_file, "r") as f:
        lines = f.readlines()

    # Find the index of the line containing '; HEADER_BLOCK_START' and '; HEADER_BLOCK_END'
    header_start = next((i for i, line in enumerate(lines) if line.strip() == '; HEADER_BLOCK_START'), None)
    header_end = next((i for i, line in enumerate(lines) if line.strip() == '; HEADER_BLOCK_END'), None)

    # Remove the header block if both start and end are found
    if header_start is not None and header_end is not None:
        del lines[header_start:header_end + 1]

    # Convert the thumbnail from PNG to JPEG
    thumbnail_start = next((i for i, line in enumerate(lines) if '; thumbnail begin' in line), None)

    if thumbnail_start is not None:
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

            # Replace the size in the '; thumbnail begin' line with the new JPEG size
            lines[thumbnail_start] = f'; thumbnail_JPG begin 250x250 {len(image_jpg_data)}\n'

            # Split the base64 string into formatted lines
            max_line_length = 79 - len("; ")
            injected_jpg_data = ["; " + image_jpg_base64[i:i + max_line_length] for i in range(0, len(image_jpg_base64), max_line_length)]

            # Replace the old PNG lines with the new JPEG lines
            lines[thumbnail_start + 1:thumbnail_end] = [line + "\n" for line in injected_jpg_data]

    # Remove all lines before '; thumbnail_JPG begin'
    # This will also remove the newlines and the solitary ';' character
    lines = [line for line in lines if not line.strip() == ';' and not line.strip() == '']
    thumbnail_jpg_index = next((i for i, line in enumerate(lines) if line.startswith('; thumbnail_JPG begin')), None)
    if thumbnail_jpg_index is not None and thumbnail_jpg_index > 0:
        # Now we remove the newline before the '; thumbnail_JPG begin'
        if lines[thumbnail_jpg_index - 1].strip() == '':
            del lines[thumbnail_jpg_index - 1]

    # Write the modified content back to the original file
    with open(source_file, "w") as f:
        f.writelines(lines)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script.py <gcode-file>")
        sys.exit(1)

    main(sys.argv[1])
