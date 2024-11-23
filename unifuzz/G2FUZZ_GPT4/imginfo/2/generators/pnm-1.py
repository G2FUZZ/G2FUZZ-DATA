import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the image data
# This pattern represents a 10x10 pixel image where 1 is black and 0 is white
# The pattern is a simple checkerboard
image_data = [
    "1 0 1 0 1 0 1 0 1 0",
    "0 1 0 1 0 1 0 1 0 1",
    "1 0 1 0 1 0 1 0 1 0",
    "0 1 0 1 0 1 0 1 0 1",
    "1 0 1 0 1 0 1 0 1 0",
    "0 1 0 1 0 1 0 1 0 1",
    "1 0 1 0 1 0 1 0 1 0",
    "0 1 0 1 0 1 0 1 0 1",
    "1 0 1 0 1 0 1 0 1 0",
    "0 1 0 1 0 1 0 1 0 1"
]

# Open the file to write binary data
with open('./tmp/simple_pattern.pbm', 'w') as file:
    # Write the header
    # P1 is the magic number for a PBM file in plain PNM format
    # 10 10 is the width and height of the image
    file.write("P1\n10 10\n")
    
    # Write the image data
    for row in image_data:
        file.write(row + '\n')