import os

# Ensure the target directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)  # Corrected argument name here

# PBM example - A simple smiley face
pbm_data = """P1
# This is an example of a PBM file representing a simple smiley face
8 8
0 0 0 0 0 0 0 0
0 1 1 0 0 1 1 0
0 1 1 0 0 1 1 0
0 0 0 0 0 0 0 0
0 1 0 0 0 0 1 0
0 0 1 1 1 1 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
"""

# PGM example - A gradient
pgm_data = """P2
# This is an example of a PGM file representing a gradient
16 8
255
0 16 32 48 64 80 96 112 128 144 160 176 192 208 224 240
16 16 32 48 64 80 96 112 128 144 160 176 192 208 224 240
32 32 48 64 80 96 112 128 144 160 176 192 208 224 240 255
48 48 64 80 96 112 128 144 160 176 192 208 224 240 255 255
64 64 80 96 112 128 144 160 176 192 208 224 240 255 255 255
80 80 96 112 128 144 160 176 192 208 224 240 255 255 255 255
96 96 112 128 144 160 176 192 208 224 240 255 255 255 255 255
"""

# PPM example - Simple RGB stripes
ppm_data = """P3
# This is an example of a PPM file representing simple RGB stripes
3 3
255
255 0 0   0 255 0   0 0 255
255 255 0 255 0 255 0 255 255
255 255 255 255 255 255 255 255 255
"""

# Saving the PNM files
with open(os.path.join(output_dir, "example.pbm"), "w") as pbm_file:
    pbm_file.write(pbm_data)

with open(os.path.join(output_dir, "example.pgm"), "w") as pgm_file:  # Corrected variable name here
    pgm_file.write(pgm_data)

with open(os.path.join(output_dir, "example.ppm"), "w") as ppm_file:  # Corrected variable name here
    ppm_file.write(ppm_data)

print("PNM files have been saved in the './tmp/' directory.")