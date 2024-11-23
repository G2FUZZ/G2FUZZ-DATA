import os

def create_bmp_file(file_path):
    # File Header: BMP files start with a 14-byte file header
    file_header = b'BM'  # Signature
    file_header += (154).to_bytes(4, byteorder='little')  # File size
    file_header += (0).to_bytes(2, byteorder='little')  # Reserved1
    file_header += (0).to_bytes(2, byteorder='little')  # Reserved2
    file_header += (154).to_bytes(4, byteorder='little')  # Pixel array offset

    with open(file_path, 'wb') as bmp_file:
        bmp_file.write(file_header)

# Create tmp directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Generate 'bmp' files with file header
for i in range(3):
    file_path = f'./tmp/test_file_{i}.bmp'
    create_bmp_file(file_path)
    print(f'{file_path} generated.')