import numpy as np

# Define the text to be encoded in the PNM file
text = "8. Widely Supported: PNM files are supported by many image processing software and libraries."

# Create a PBM file
def create_pbm(text, filename):
    # Convert text to binary
    binary_data = ' '.join(format(ord(char), '08b') for char in text)
    height = 1
    width = len(binary_data)
    
    # Write the PBM file
    with open(filename, 'w') as file:
        file.write("P1\n")
        file.write(f"{width} {height}\n")
        file.write(binary_data)

# Create a PGM file
def create_pgm(text, filename):
    # Convert text to grayscale values
    grayscale_values = [ord(char) for char in text]
    max_value = max(grayscale_values)
    height = 1
    width = len(grayscale_values)
    
    # Write the PGM file
    with open(filename, 'w') as file:
        file.write("P2\n")
        file.write(f"{width} {height}\n")
        file.write(f"{max_value}\n")
        file.write(' '.join(map(str, grayscale_values)))

# Create a PPM file
def create_ppm(text, filename):
    # Generate random RGB values for each character
    np.random.seed(0)
    rgb_values = np.random.randint(0, 256, size=(len(text), 3))
    height = 1
    width = len(text)
    
    # Write the PPM file
    with open(filename, 'w') as file:
        file.write("P3\n")
        file.write(f"{width} {height}\n")
        file.write("255\n")
        for rgb in rgb_values:
            file.write(' '.join(map(str, rgb)) + ' ')

# Save the PNM files in ./tmp/
create_pbm(text, './tmp/file.pbm')
create_pgm(text, './tmp/file.pgm')
create_ppm(text, './tmp/file.ppm')