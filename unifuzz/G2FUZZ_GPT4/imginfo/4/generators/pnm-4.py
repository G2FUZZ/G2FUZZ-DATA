import os

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a PBM file (Portable Bitmap)
def generate_pbm(filename):
    header = "P1\n# This is a PBM example\n5 5\n"
    data = [
        "1 0 1 0 1",
        "0 1 0 1 0",
        "1 0 1 0 1",
        "0 1 0 1 0",
        "1 0 1 0 1"
    ]
    with open(filename, 'w') as f:
        f.write(header + "\n".join(data))

# Function to generate a PGM file (Portable Graymap)
def generate_pgm(filename):
    header = "P2\n# This is a PGM example\n5 5\n255\n"
    data = [
        "255 100 255 100 255",
        "100 255 100 255 100",
        "255 100 255 100 255",
        "100 255 100 255 100",
        "255 100 255 100 255"
    ]
    with open(filename, 'w') as f:
        f.write(header + "\n".join(data))

# Function to generate a PPM file (Portable Pixmap)
def generate_ppm(filename):
    header = "P3\n# This is a PPM example\n5 5\n255\n"
    data = [
        "255 0 0  0 255 0  0 0 255  255 255 0  255 0 255",
        "0 255 0  255 0 0  255 255 255  0 0 255  0 255 255",
        "0 0 255  255 0 255  0 255 0  255 0 0  255 255 255",
        "255 255 0  0 255 255  255 0 0  0 255 0  0 0 255",
        "255 0 255  255 255 255  0 255 0  255 0 0  0 255 255"
    ]
    with open(filename, 'w') as f:
        f.write(header + "\n".join(data))

# Generate the files
generate_pbm('./tmp/example.pbm')
generate_pgm('./tmp/example.pgm')
generate_ppm('./tmp/example.ppm')

print("PNM files generated successfully.")