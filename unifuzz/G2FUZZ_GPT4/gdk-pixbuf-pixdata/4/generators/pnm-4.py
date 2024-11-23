import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a simple PBM file (black and white)
pbm_data = "P1\n# This is a simple PBM example\n5 5\n0 1 0 1 0\n1 0 1 0 1\n0 1 0 1 0\n1 0 1 0 1\n0 1 0 1 0"
with open('./tmp/example.pbm', 'w') as file:
    file.write(pbm_data)

# Generate a simple PPM file (RGB color)
ppm_data = "P3\n# This is a simple PPM example\n3 2\n255\n255 0 0  0 255 0  0 0 255\n255 255 0  255 255 255  0 0 0"
with open('./tmp/example.ppm', 'w') as file:
    file.write(ppm_data)

print("PNM files have been generated and saved in ./tmp/")