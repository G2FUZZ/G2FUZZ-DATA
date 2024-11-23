import os

# Function to generate complex PNM files
def generate_complex_pnm_files():
    header = "P3\n# This is a comment\n5 5\n255\n"
    pixels = "255 0 0 0 255 0 0 0 255 255 255 255 255 255 255 0 0 0 0 0 255 0 0 0 0 255 255 255 255 255 255 255 255 255 0 0 0 0 0 255 0 0 0 0 255\n"
    filename = "complex_file.pnm"
    directory = "./tmp/"

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(os.path.join(directory, filename), "w") as file:
        file.write(header)
        file.write(pixels)

# Generate complex PNM files
generate_complex_pnm_files()