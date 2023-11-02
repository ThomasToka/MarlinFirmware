#!/usr/bin/env python3
#
# Orca Slicer remove headers before jpg.
#
# This script has been developed for E3S1PROFORKBYTT by Thomas Toka.
#
# ------------------------------------------------------------------------------

import sys
import base64
from PIL import Image
from io import BytesIO

# Get the g-code source file name
sourceFile = sys.argv[1]

# Read the ENTIRE g-code file into memory
with open(sourceFile, "r") as f:
    lines = f.readlines()

# Find the index of the line containing '; HEADER_BLOCK_START'
header_start = None
for i, line in enumerate(lines):
    if line.strip() == '; HEADER_BLOCK_START':
        header_start = i
        break

# Find the index of the line containing '; THUMBNAIL_BLOCK_START'
thumbnail_start = None
for i, line in enumerate(lines):
    if line.strip() == '; THUMBNAIL_BLOCK_START':
        thumbnail_start = i
        break

# Ensure both start markers were found for header and thumbnail
if header_start is not None and thumbnail_start is not None:
    # Remove the lines between '; HEADER_BLOCK_START' and '; THUMBNAIL_BLOCK_START' including the marker lines
    del lines[header_start:thumbnail_start+1]

    # Find the index of the line containing '; thumbnail begin' or a similar line
    index_begin = None
    for i, line in enumerate(lines):
        if '; thumbnail begin' in line:
            index_begin = i
            break

    # Find the index of the line containing '; thumbnail end'
    index_end = None
    for i, line in enumerate(lines[index_begin:], start=index_begin):
        if line.strip() == '; thumbnail end':
            index_end = i
            break

    # Ensure both start and end markers were found for thumbnail
    if index_begin is not None and index_end is not None:
        # Extract the original PNG data from the lines between '; thumbnail begin' and '; thumbnail end'
        original_png_data = "".join(lines[index_begin + 1:index_end])

        # Remove "; " from the extracted PNG data
        original_png_data = original_png_data.replace("; ", "")

        try:
            # Decode the original PNG data
            png_data_bytes = base64.b64decode(original_png_data)
            image = Image.open(BytesIO(png_data_bytes))
            image = image.convert("RGB")  # Convert to RGB mode

            # Encode the image as JPEG
            buffer = BytesIO()
            image.save(buffer, format="JPEG")
            image_jpg_data = buffer.getvalue()

            # Base64 encode the JPEG data
            image_jpg_base64 = base64.b64encode(image_jpg_data).decode('utf-8')

            # Calculate the size of the JPEG data in bytes
            jpg_data_size = len(image_jpg_base64)

            # Replace the size in the '; thumbnail begin' line
            lines[index_begin] = f'; thumbnail begin 250x250 {jpg_data_size}\n'

            # Calculate the maximum line length
            max_line_length = 79 - len("; ")

            # Prepare the injected JPEG data with each line on a new line
            injected_jpg_data = ["; " + image_jpg_base64[i:i + max_line_length] for i in range(0, len(image_jpg_base64), max_line_length)]

            # Insert the new formatted JPEG data into the original lines
            lines[index_begin + 1:index_end] = [line + "\n" for line in injected_jpg_data]

            # Write the modified content back to the original file
            with open(sourceFile, "w") as f:
                f.writelines(lines)
        except Exception as e:
            sys.exit(1)
