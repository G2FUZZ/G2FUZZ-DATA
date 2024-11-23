import os

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Function to create PBM file (a simple black and white image)
def create_pbm(filename):
    with open(filename, 'w') as f:
        f.write("P1\n")  # Magic number for PBM
        f.write("# This is a simple PBM file\n")  # Optional comment
        f.write("5 5\n")  # Width and height
        # Image data: 1 is black, 0 is white
        data = [
            "0 1 1 1 0",
            "1 0 0 0 1",
            "1 0 1 0 1",
            "1 0 0 0 1",
            "0 1 1 1 0"
        ]
        f.write("\n".join(data))

# Function to create PGM file (a simple grayscale image)
def create_pgm(filename):
    with open(filename, 'w') as f:
        f.write("P2\n")  # Magic number for PGM
        f.write("# This is a simple PGM file\n")  # Optional comment
        f.write("5 5\n")  # Width and height
        f.write("255\n")  # Max grayscale value
        # Image data: values from 0 (black) to 255 (white)
        data = [
            "255 100 50 100 255",
            "100 255 200 255 100",
            "50 200 255 200 50",
            "100 255 200 255 100",
            "255 100 50 100 255"
        ]
        f.write("\n".join(data))

# Function to create PPM file (a simple RGB image)
def create_ppm(filename):
    with open(filename, 'w') as f:
        f.write("P3\n")  # Magic number for PPM
        f.write("# This is a simple PPM file\n")  # Optional comment
        f.write("5 5\n")  # Width and height
        f.write("255\n")  # Max color value
        # Image data: RGB triples
        data = [
            "255 0 0  0 255 0  0 0 255  255 255 0  0 255 255",
            "0 255 0  255 0 0  0 255 255  255 0 255  255 255 0",
            "0 0 255  255 255 0  255 0 255  0 255 255  255 0 0",
            "0 255 255  255 0 255  255 255 0  255 0 0  0 255 0",
            "255 255 0  0 255 255  255 0 0  0 0 255  255 255 255"
        ]
        f.write("\n".join(data))

# Generate the files
create_pbm('./tmp/example.pbm')
create_pgm('./tmp/example.pgm')
create_ppm('./tmp/example.ppm')

print("PNM files generated successfully.")