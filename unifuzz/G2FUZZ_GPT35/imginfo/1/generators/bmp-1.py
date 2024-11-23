import os

def generate_bmp_file(file_path):
    # File Header (54 bytes)
    file_header = b'BM'  # Signature
    file_header += (1546).to_bytes(4, byteorder='little')  # File size (dummy value)
    file_header += (0).to_bytes(2, byteorder='little')  # Reserved (dummy value)
    file_header += (54).to_bytes(4, byteorder='little')  # Pixel data offset
    
    # Create the bmp file
    with open(file_path, 'wb') as bmp_file:
        bmp_file.write(file_header)
    
    print(f"BMP file generated at {file_path}")

# Create a directory to store the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a BMP file
generate_bmp_file('./tmp/generated.bmp')