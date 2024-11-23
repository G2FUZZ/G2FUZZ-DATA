import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate PBM ASCII (P1)
pbm_ascii_content = "P1\n# This is an example of a PBM file in ASCII\n2 2\n1 0\n0 1\n"
with open('./tmp/example_ascii.pbm', 'w') as file:
    file.write(pbm_ascii_content)

# Generate PBM Binary (P4)
pbm_binary_content = bytes([0b10000000, 0b00000000])  # Example pattern for 2x2
with open('./tmp/example_binary.pbm', 'wb') as file:
    file.write(b"P4\n2 2\n" + pbm_binary_content)

# Generate PGM ASCII (P2)
pgm_ascii_content = "P2\n# This is an example of a PGM file in ASCII\n2 2\n255\n0 255\n255 0\n"
with open('./tmp/example_ascii.pgm', 'w') as file:
    file.write(pgm_ascii_content)

# Generate PGM Binary (P5)
pgm_binary_content = bytes([0, 255, 255, 0])  # Gradient example
with open('./tmp/example_binary.pgm', 'wb') as file:
    file.write(b"P5\n2 2\n255\n" + pgm_binary_content)

# Generate PPM ASCII (P3)
ppm_ascii_content = "P3\n# This is an example of a PPM file in ASCII\n2 2\n255\n255 0 0  0 255 0\n0 0 255  255 255 0\n"
with open('./tmp/example_ascii.ppm', 'w') as file:
    file.write(ppm_ascii_content)

# Generate PPM Binary (P6)
ppm_binary_content = bytes([255, 0, 0, 0, 255, 0, 0, 0, 255, 255, 255, 0])  # RGB and Yellow example
with open('./tmp/example_binary.ppm', 'wb') as file:
    file.write(b"P6\n2 2\n255\n" + ppm_binary_content)