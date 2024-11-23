import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# PBM example - simple black and white image
pbm_data = """P1
# This is an example of a PBM file
4 4
0 1 0 1
1 0 1 0
0 1 0 1
1 0 1 0
"""
with open('./tmp/example.pbm', 'w') as f:
    f.write(pbm_data)

# PGM example - simple gradient from black to white
pgm_data = """P2
# This is an example of a PGM file
4 4
255
0 64 128 255
64 64 128 255
128 128 128 255
255 255 255 255
"""
with open('./tmp/example.pgm', 'w') as f:
    f.write(pgm_data)

# PPM example - simple RGB image
ppm_data = """P3
# This is an example of a PPM file
4 4
255
255 0 0   0 255 0   0 0 255   255 255 0
255 255 0   255 0 0   0 255 0   0 0 255
0 0 255   255 255 0   255 0 0   0 255 0
0 255 0   0 0 255   255 255 0   255 0 0
"""
with open('./tmp/example.ppm', 'w') as f:
    f.write(ppm_data)

print("PNM files generated successfully.")