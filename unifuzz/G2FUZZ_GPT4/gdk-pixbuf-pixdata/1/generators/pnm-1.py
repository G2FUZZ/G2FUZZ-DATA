import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# PBM file generation (Simple pattern)
pbm_data = """
P1
# This is an example of a PBM file
4 4
0 1 0 1
1 0 1 0
0 1 0 1
1 0 1 0
"""
with open('./tmp/example.pbm', 'w') as file:
    file.write(pbm_data.strip())

# PGM file generation (Gradient)
pgm_data = [
    "P2",
    "# This is an example of a PGM file",
    "4 4",
    "255"
]
pgm_data.extend([" ".join([str((x+y)*16) for x in range(4)]) for y in range(4)])
with open('./tmp/example.pgm', 'w') as file:
    file.write("\n".join(pgm_data))

# PPM file generation (Simple colored pattern)
ppm_data = """
P3
# This is an example of a PPM file
4 4
255
255 0 0   0 255 0   0 0 255   255 255 0
0 255 255 255 0 255 0 0 0     255 255 255
255 0 255 255 255 255 0 0 255 0 0
0 255 0   255 0 255 0 255 255 255 255 255
"""
with open('./tmp/example.ppm', 'w') as file:
    file.write(ppm_data.strip())