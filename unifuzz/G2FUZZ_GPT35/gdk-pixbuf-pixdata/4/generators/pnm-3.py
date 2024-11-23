import os

# Function to create a PNM file in ASCII format
def create_pnm_ascii(file_path):
    with open(file_path, 'w') as file:
        file.write("P3\n")
        file.write("# This is a P3 PNM file in ASCII format\n")
        file.write("3 2\n")
        file.write("255\n")
        file.write("255 0 0 0 255 0 0 0 255\n")
        file.write("0 255 0 255 0 255 255 255 255\n")

# Function to create a PNM file in binary format
def create_pnm_binary(file_path):
    with open(file_path, 'wb') as file:
        file.write(b'P6\n')
        file.write(b'# This is a P6 PNM file in binary format\n')
        file.write(b'3 2\n')
        file.write(b'255\n')
        file.write(bytes([255, 0, 0, 0, 255, 0, 0, 0, 255, 0, 255, 0, 255, 0, 255, 255, 255, 255]))

# Create 'tmp' directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Create PNM files in ASCII and binary formats
create_pnm_ascii('./tmp/ascii_file.pnm')
create_pnm_binary('./tmp/binary_file.pnm')