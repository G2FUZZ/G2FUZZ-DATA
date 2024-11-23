import os
import numpy as np

def create_pgx_file(file_path, width, height, bit_depth):
    """
    Generates a .pgx file with specified dimensions and bit depth.
    
    Parameters:
    - file_path: Path to save the .pgx file.
    - width: Width of the image.
    - height: Height of the image.
    - bit_depth: Bit depth per component (8, 16).
    """
    # Ensure the tmp directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Define the maximum value based on bit depth
    max_value = 2**bit_depth - 1
    
    # Create a gradient image data from 0 to max_value
    image_data = np.linspace(0, max_value, num=width*height, dtype=np.uint16).reshape((height, width))
    
    # Open file in binary write mode
    with open(file_path, 'wb') as file:
        # Write header
        header = f'PG ML {width} {height} {bit_depth}\n'.encode()
        file.write(header)
        
        # Write image data
        for row in image_data:
            if bit_depth == 16:
                file.write(row.tobytes())
            elif bit_depth == 8:
                file.write(row.astype(np.uint8).tobytes())
            else:
                raise ValueError("Unsupported bit depth. Choose 8 or 16.")

# Example usage
pgx_file_path = './tmp/example.pgx'
create_pgx_file(pgx_file_path, width=256, height=256, bit_depth=16)