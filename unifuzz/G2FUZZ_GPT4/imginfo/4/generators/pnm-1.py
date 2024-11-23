import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Path to the output PBM file
output_file_path = os.path.join(output_dir, "checkerboard.pbm")

# PBM file content
# PBM header: P1 indicates it's a PBM file in plain format, followed by the image dimensions (8x8)
# The grid represents a simple checkerboard pattern
pbm_content = """
P1
8 8
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
""".strip()

# Write the PBM content to the file
with open(output_file_path, 'w') as file:
    file.write(pbm_content)

print(f"Generated PBM file saved to {output_file_path}")