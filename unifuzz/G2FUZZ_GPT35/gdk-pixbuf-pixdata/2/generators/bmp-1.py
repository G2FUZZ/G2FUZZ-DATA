import os

def create_bmp_file(file_path):
    # Define the BMP file header
    file_header = b'BM'  # File type
    file_header += (154).to_bytes(4, byteorder='little')  # File size (54 bytes for header + 100 bytes placeholder for pixel data)
    file_header += (54).to_bytes(4, byteorder='little')  # Offset to pixel data

    with open(file_path, 'wb') as bmp_file:
        bmp_file.write(file_header)
        
    print(f'BMP file created: {file_path}')

# Create a directory to save the BMP files
os.makedirs('./tmp/', exist_ok=True)

# Generate a BMP file with the specified file header
create_bmp_file('./tmp/example.bmp')