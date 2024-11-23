import os

# Function to generate TGA file with specific file header structure
def generate_tga_file(file_name):
    file_path = f'./tmp/{file_name}.tga'
    with open(file_path, 'wb') as file:
        # Write TGA file header structure
        file.write(b'\x00' * 12)  # ID Length, Color Map Type, Image Type - Set to 0 for simplicity
        file.write(b'\x00\x00')    # Color Map Specification
        file.write(b'\x00\x00')    # Origin X
        file.write(b'\x00\x00')    # Origin Y
        file.write(b'\x00\x00')    # Image Width
        file.write(b'\x00\x00')    # Image Height
        file.write(b'\x08')        # Image Pixel Depth - Set to 8 bits
        file.write(b'\x20')        # Image Descriptor - Set to 0x20 for simplicity

    print(f'TGA file "{file_name}.tga" generated successfully.')

# Create tmp directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Generate TGA files with specific file header structure
generate_tga_file('sample_tga_file')