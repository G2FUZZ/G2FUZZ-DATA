import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a PBM file (black and white)
def generate_pbm(filename):
    with open(filename, 'w') as file:
        file.write("P1\n")
        file.write("# This is a PBM file\n")
        file.write("5 5\n")
        file.write("0 1 0 1 0\n")
        file.write("1 0 1 0 1\n")
        file.write("0 1 0 1 0\n")
        file.write("1 0 1 0 1\n")
        file.write("0 1 0 1 0\n")

# Function to generate a PGM file (grayscale)
def generate_pgm(filename):
    with open(filename, 'w') as file:
        file.write("P2\n")
        file.write("# This is a PGM file\n")
        file.write("5 5\n")
        file.write("255\n")
        for i in range(5):
            for j in range(5):
                file.write(f"{i*50 + j*10} ")
            file.write("\n")

# Function to generate a PPM file (color)
def generate_ppm(filename):
    with open(filename, 'w') as file:
        file.write("P3\n")
        file.write("# This is a PPM file\n")
        file.write("5 5\n")
        file.write("255\n")
        for i in range(5):
            for j in range(5):
                file.write(f"{i*50} {j*10} {(i+j)*20} ")
            file.write("\n")

# Generate the files
generate_pbm('./tmp/sample.pbm')
generate_pgm('./tmp/sample.pgm')
generate_ppm('./tmp/sample.ppm')

print("PNM files generated successfully.")