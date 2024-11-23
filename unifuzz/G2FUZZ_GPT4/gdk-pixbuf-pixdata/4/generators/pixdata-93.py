import numpy as np
import struct
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a header for our custom pixdata file
def create_header(bit_depth, width, height):
    # File signature "PXDT" (PixData), version 1
    signature = b'PXDT'
    version = 1
    header_struct = struct.Struct('<4sBHHH')  # < indicates little-endian, 4s for signature, B for version, H for unsigned short
    return header_struct.pack(signature, version, bit_depth, width, height)

# Function to generate and save a pixdata file with specified bit depth
def generate_pixdata_file(bit_depth, width=256, height=256):
    # Calculate the maximum value for the given bit depth
    max_val = 2**bit_depth - 1
    
    # Generate a gradient image
    gradient = np.tile(np.linspace(0, max_val, width, dtype=np.uint16), (height, 1))

    # Prepare pixel data according to bit depth
    if bit_depth <= 8:
        pixel_data = gradient.astype(np.uint8).tobytes()
    elif bit_depth <= 16:
        pixel_data = gradient.astype(np.uint16).tobytes()
    else:
        raise ValueError("Unsupported bit depth, must be 16 or lower for this example")

    # Create file header
    header = create_header(bit_depth, width, height)
    
    # File path
    file_path = f'./tmp/image_{bit_depth}bit.pxd'
    
    # Write header and pixel data to file
    with open(file_path, 'wb') as file:
        file.write(header)
        file.write(pixel_data)
    
    print(f"Saved {file_path}")

# Generate pixdata files for 8-bit and 16-bit depths
generate_pixdata_file(8)
generate_pixdata_file(16)