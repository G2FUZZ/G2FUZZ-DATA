import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# PBM ASCII (P1) and Binary (P4)
pbm_ascii_data = "P1\n# This is an example of a PBM file in ASCII\n5 5\n1 0 1 0 1\n0 1 0 1 0\n1 0 1 0 1\n0 1 0 1 0\n1 0 1 0 1\n"
pbm_binary_data = b"P4\n5 5\n\xAA\x55\xAA\x55\xAA"

with open('./tmp/example_pbm_ascii.pbm', 'w') as file:
    file.write(pbm_ascii_data)

with open('./tmp/example_pbm_binary.pbm', 'wb') as file:
    file.write(pbm_binary_data)

# PGM ASCII (P2) and Binary (P5)
pgm_ascii_data = "P2\n# This is an example of a PGM file in ASCII\n5 5\n255\n0 64 128 192 255\n255 192 128 64 0\n0 64 128 192 255\n255 192 128 64 0\n0 64 128 192 255\n"
pgm_binary_data = b"P5\n5 5\n255\n" + bytes([0, 64, 128, 192, 255, 255, 192, 128, 64, 0, 0, 64, 128, 192, 255, 255, 192, 128, 64, 0, 0, 64, 128, 192, 255])

with open('./tmp/example_pgm_ascii.pgm', 'w') as file:
    file.write(pgm_ascii_data)

with open('./tmp/example_pgm_binary.pgm', 'wb') as file:
    file.write(pgm_binary_data)

# PPM ASCII (P3) and Binary (P6)
ppm_ascii_data = "P3\n# This is an example of a PPM file in ASCII\n2 2\n255\n255 0 0  0 255 0\n0 0 255  255 255 0\n"
ppm_binary_data = b"P6\n2 2\n255\n" + bytes([255, 0, 0, 0, 255, 0, 0, 0, 255, 255, 255, 0])

with open('./tmp/example_ppm_ascii.ppm', 'w') as file:
    file.write(ppm_ascii_data)

with open('./tmp/example_ppm_binary.ppm', 'wb') as file:
    file.write(ppm_binary_data)