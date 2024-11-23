import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)  # Corrected argument name

# Function to generate a PBM file
def generate_pbm(filename):
    header = "P1\n"  # PBM ASCII format
    width, height = 5, 5
    data = [
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0]
    ]
    with open(filename, 'w') as file:
        file.write(f"{header}{width} {height}\n")
        for row in data:
            file.write(' '.join(str(pixel) for pixel in row) + '\n')

# Function to generate a PGM file
def generate_pgm(filename):
    header = "P2\n"  # PGM ASCII format
    width, height = 5, 5
    max_val = 255
    data = [
        [0, 123, 255, 123, 0],
        [123, 255, 255, 255, 123],
        [255, 255, 255, 255, 255],
        [123, 255, 255, 255, 123],
        [0, 123, 255, 123, 0]
    ]
    with open(filename, 'w') as file:
        file.write(f"{header}{width} {height}\n{max_val}\n")
        for row in data:
            file.write(' '.join(str(pixel) for pixel in row) + '\n')

# Function to generate a PPM file
def generate_ppm(filename):
    header = "P3\n"  # PPM ASCII format
    width, height = 2, 2
    max_val = 255
    data = [
        [[255, 0, 0], [0, 255, 0]],
        [[0, 0, 255], [255, 255, 0]]
    ]
    with open(filename, 'w') as file:
        file.write(f"{header}{width} {height}\n{max_val}\n")
        for row in data:
            for pixel in row:
                file.write(' '.join(str(color) for color in pixel) + '  ')
            file.write('\n')

# Generate files
generate_pbm('./tmp/example.pbm')
generate_pgm('./tmp/example.pgm')
generate_ppm('./tmp/example.ppm')

print("PNM files generated successfully.")