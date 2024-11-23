import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate PBM file (simple binary image)
pbm_data = "P1\n# This is a PBM example\n2 2\n0 1\n1 0"
with open('./tmp/example.pbm', 'w') as file:
    file.write(pbm_data)

# Generate PGM file (simple gradient)
pgm_data = "P2\n# This is a PGM example\n4 4\n255\n"
pgm_data += "\n".join([" ".join([str((i+j)*16) for i in range(4)]) for j in range(4)])
with open('./tmp/example.pgm', 'w') as file:
    file.write(pgm_data)

# Generate PPM file (simple RGB image)
ppm_data = "P3\n# This is a PPM example\n2 2\n255\n"
ppm_data += "255 0 0  0 255 0\n0 0 255  255 255 0\n"
with open('./tmp/example.ppm', 'w') as file:
    file.write(ppm_data)

print("PNM files generated in ./tmp/")