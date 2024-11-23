import os

def create_bmp_file(file_path):
    # File Header
    file_header = b'BM'  # Signature
    file_size = 54  # Total file size in bytes
    reserved_bytes = b'\x00\x00\x00\x00'
    data_offset = 54  # Offset where pixel data starts

    with open(file_path, 'wb') as file:
        # Write File Header
        file.write(file_header)
        file.write(file_size.to_bytes(4, 'little'))
        file.write(reserved_bytes)
        file.write(data_offset.to_bytes(4, 'little'))

# Create a 'tmp' directory if it doesn't already exist
os.makedirs('./tmp/', exist_ok=True)

# Generate and save a BMP file with the specified features
create_bmp_file('./tmp/generated.bmp')