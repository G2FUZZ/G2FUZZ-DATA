import os

# Create the temporary directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# ASCII PBM Example
pbm_ascii_content = """P1
# This is an example of a PBM file in ASCII format
4 4
0 1 0 1
1 0 1 0
0 1 0 1
1 0 1 0
"""
with open('./tmp/example_ascii.pbm', 'w') as f:
    f.write(pbm_ascii_content)

# Binary PBM Example
pbm_binary_content = bytes([0x50, 0x34, 0x0A, 0x34, 0x20, 0x34, 0x0A, 0x0A, 0b01010100, 0b10101010, 0b01010100, 0b10101010])
with open('./tmp/example_binary.pbm', 'wb') as f:
    f.write(pbm_binary_content)

# ASCII PGM Example
pgm_ascii_content = """P2
# This is an example of a PGM file in ASCII format
2 2
255
100 150
200 250
"""
with open('./tmp/example_ascii.pgm', 'w') as f:
    f.write(pgm_ascii_content)

# Binary PGM Example
pgm_binary_content = b'P5\n2 2\n255\n' + bytes([100, 150, 200, 250])
with open('./tmp/example_binary.pgm', 'wb') as f:
    f.write(pgm_binary_content)

# ASCII PPM Example
ppm_ascii_content = """P3
# This is an example of a PPM file in ASCII format
2 2
255
255 0 0  0 255 0
0 0 255  255 255 0
"""
with open('./tmp/example_ascii.ppm', 'w') as f:
    f.write(ppm_ascii_content)

# Binary PPM Example
ppm_binary_content = b'P6\n2 2\n255\n' + bytes([255, 0, 0, 0, 255, 0, 0, 0, 255, 255, 255, 0])
with open('./tmp/example_binary.ppm', 'wb') as f:
    f.write(ppm_binary_content)

print("PNM files have been generated in ./tmp/")