#!/usr/bin/env python3
#
# Orca Slicer remove headers before jpg.
#
# This script has been developed for E3S1PROFORKBYTT by Thomas Toka.
#
# ------------------------------------------------------------------------------

import sys
import os

# Get the g-code source file name
sourceFile = sys.argv[1]

# Read the ENTIRE g-code file into memory
with open(sourceFile, "r") as f:
    lines = f.readlines()

new_lines = []
remove_lines = False

for line in lines:
    if line.strip() == '; HEADER_BLOCK_START':
        remove_lines = True
    elif line.strip() == '; THUMBNAIL_BLOCK_START':
        remove_lines = False
    elif not remove_lines:
        new_lines.append(line)

try:
    with open(sourceFile, "w+") as of:
        of.write(''.join(new_lines))
except Exception as e:
    print(f'Error writing output file: {str(e)}')
    input()
finally:
    of.close()
    f.close()