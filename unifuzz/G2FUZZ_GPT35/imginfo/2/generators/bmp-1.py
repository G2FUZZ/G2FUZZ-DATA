import os

def create_bmp_file(file_path):
    # File Header: BMP files begin with a file header containing information such as the file type and size
    file_header = b'BM'  # Bitmap file header
    file_size = 54  # Assuming a simple BMP file with no image data

    with open(file_path, 'wb') as bmp_file:
        bmp_file.write(file_header)
        bmp_file.write(file_size.to_bytes(4, byteorder='little'))  # Write file size as 4 bytes little-endian

# Create tmp directory if it doesn't exist
os.makedirs('tmp', exist_ok=True)

# Generate BMP file with file header
bmp_file_path = './tmp/test.bmp'
create_bmp_file(bmp_file_path)