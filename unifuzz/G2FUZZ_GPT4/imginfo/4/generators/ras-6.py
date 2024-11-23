import struct
import os

def create_ras_file(filename, width, height, depth, data_type):
    """
    Create a RAS file with specified metadata and save it to ./tmp/ directory.

    Parameters:
    - filename: Name of the file to be saved (string).
    - width: Width of the image in pixels (int).
    - height: Height of the image in pixels (int).
    - depth: Color depth in bits per pixel (int).
    - data_type: Type of raster data (int).
    """
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # RAS file magic number (always 0x59a66a95)
    magic_number = 0x59a66a95

    # Length of the image data (dummy data for this example)
    length = width * height * (depth // 8)

    # RAS file header format: magic (4 bytes), width (4 bytes), height (4 bytes),
    # depth (4 bytes), length (4 bytes), type (4 bytes), maptype (4 bytes), maplength (4 bytes)
    header = struct.pack('>IIIIIIII', magic_number, width, height, depth, length, data_type, 0, 0)

    # Create the RAS file with the specified header
    with open(f'./tmp/{filename}', 'wb') as file:
        file.write(header)
        # Writing dummy data as image data
        file.write(b'\x00' * length)

# Example of creating a RAS file
create_ras_file('example.ras', 800, 600, 24, 1)  # Standard RGB image