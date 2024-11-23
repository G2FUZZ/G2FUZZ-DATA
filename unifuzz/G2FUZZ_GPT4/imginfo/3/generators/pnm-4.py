import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Path to the output PNM file
output_path = os.path.join(output_dir, 'example.pbm')

# PBM header for a small 10x10 image
# P1 indicates it's a PBM, followed by width and height
pbm_header = 'P1\n10 10\n'

# Generating a simple pattern for the PBM file
# 0 is white, 1 is black
pbm_data = [
    '0 1 0 1 0 1 0 1 0 1',
    '1 0 1 0 1 0 1 0 1 0',
    '0 1 0 1 0 1 0 1 0 1',
    '1 0 1 0 1 0 1 0 1 0',
    '0 1 0 1 0 1 0 1 0 1',
    '1 0 1 0 1 0 1 0 1 0',
    '0 1 0 1 0 1 0 1 0 1',
    '1 0 1 0 1 0 1 0 1 0',
    '0 1 0 1 0 1 0 1 0 1',
    '1 0 1 0 1 0 1 0 1 0',
]

# Combine the header and data into one string
pbm_content = pbm_header + '\n'.join(pbm_data)

# Write the PBM content to a file
with open(output_path, 'w') as file:
    file.write(pbm_content)

print(f"PBM file created at: {output_path}")