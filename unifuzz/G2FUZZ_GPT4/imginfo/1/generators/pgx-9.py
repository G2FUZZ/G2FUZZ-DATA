import numpy as np
import os

def create_pgx_file(filename, width, height, bit_depth):
    """
    Creates a PGX file with a gradient demonstrating bit-depth support.

    Parameters:
    - filename: Name of the file to save, including path.
    - width: Width of the image.
    - height: Height of the image.
    - bit_depth: Bit depth of the image.
    """
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Generate a gradient image
    max_val = 2**bit_depth - 1
    img = np.tile(np.linspace(0, max_val, width, dtype=np.uint16), (height, 1))
    
    # Open file in binary mode to write
    with open(filename, 'wb') as file:
        # Write the PGX header
        # PGX format specifies endianess, bit depth, width, and height at the start of the file.
        # Here we assume little-endian format for simplicity.
        header = f'PG ML {bit_depth} {width} {height}\n'.encode()
        file.write(header)
        
        # Write the image data
        if bit_depth > 8:
            # For bit depths greater than 8, data is stored as 16-bit integers
            img_bytes = img.astype(np.uint16).tobytes()
        else:
            # For 8 bits or less, data is stored as 8-bit integers
            img_bytes = img.astype(np.uint8).tobytes()
        
        file.write(img_bytes)
        
# Example usage
create_pgx_file('./tmp/example.pgx', 256, 256, 16)