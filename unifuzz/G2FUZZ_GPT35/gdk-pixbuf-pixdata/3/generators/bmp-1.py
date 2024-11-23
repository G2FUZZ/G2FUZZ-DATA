import os

def generate_bmp_file(file_path):
    # Create a BMP file header
    file_header = bytearray(b'BM')  # BMP file magic number
    file_size = 54  # Total size of the file header (assuming no image data)

    # Update the file size in the header
    file_header.extend(file_size.to_bytes(4, byteorder='little'))

    # Save the file to the specified path
    with open(file_path, 'wb') as file:
        file.write(file_header)

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a BMP file with the file header
file_path = './tmp/sample.bmp'
generate_bmp_file(file_path)
print(f'BMP file generated at: {file_path}')