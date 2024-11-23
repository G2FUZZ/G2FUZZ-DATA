import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)  # Corrected the typo here

# Path to save the PNM file
file_path = './tmp/sample.pbm'

# PBM header for a small 3x3 black and white image
# P1 indicates it's a PBM file in plain format
# "3 3" is the width and height of the image
# The matrix represents the pixels (0: white, 1: black)
pbm_data = """
P1
3 3
0 1 0
1 0 1
0 1 0
""".strip()

# Write the PBM data to a file
with open(file_path, 'w') as file:
    file.write(pbm_data)

print(f"File saved to {file_path}")