import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# ASCII PBM
pbm_ascii_data = "P1\n# This is an example of a PBM file in ASCII format\n3 3\n0 1 0\n1 0 1\n0 1 0"
with open('./tmp/pbm_ascii.pbm', 'w') as file:
    file.write(pbm_ascii_data)

# Binary PBM
pbm_binary_data = bytearray([0b01010101, 0b10101010, 0b01010101])
with open('./tmp/pbm_binary.pbm', 'wb') as file:
    file.write(b'P4\n3 3\n' + pbm_binary_data)

# ASCII PGM
pgm_ascii_data = "P2\n# This is an example of a PGM file in ASCII format\n2 2\n255\n0 255\n255 0"
with open('./tmp/pgm_ascii.pgm', 'w') as file:
    file.write(pgm_ascii_data)

# Binary PGM
pgm_binary_data = bytearray([0, 255, 255, 0])
with open('./tmp/pgm_binary.pgm', 'wb') as file:
    file.write(b'P5\n2 2\n255\n' + pgm_binary_data)

# ASCII PPM
ppm_ascii_data = "P3\n# This is an example of a PPM file in ASCII format\n2 2\n255\n255 0 0 0 255 0\n0 0 255 255 255 255"
with open('./tmp/ppm_ascii.ppm', 'w') as file:
    file.write(ppm_ascii_data)

# Binary PPM
ppm_binary_data = bytearray([255, 0, 0, 0, 255, 0, 0, 0, 255, 255, 255, 255])
with open('./tmp/ppm_binary.ppm', 'wb') as file:
    file.write(b'P6\n2 2\n255\n' + ppm_binary_data)

print("PNM files have been generated and saved in ./tmp/")