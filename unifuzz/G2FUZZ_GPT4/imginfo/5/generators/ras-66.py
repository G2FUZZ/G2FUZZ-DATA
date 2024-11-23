import numpy as np
import struct
import os

def create_ras_header(width, height, depth=24, rle=False):
    """
    Creates a Sun Raster file header.
    
    Parameters:
    - width: The width of the image.
    - height: The height of the image.
    - depth: Bit depth (default 24 for RGB).
    - rle: Boolean indicating if RLE compression is used (not implemented in this function).
    
    Returns:
    - A bytes object containing the header.
    """
    MAGIC_NUMBER = 0x59a66a95  # Magic number for Sun Raster files
    ras_type = 1 if rle else 0  # Type: 0 = Standard, 1 = RLE encoded
    maptype = 0  # Color map type: 0 = Direct color
    maplength = 0  # Length of color map in bytes
    
    # Corrected header structure: magic, width, height, depth, length, type, maptype, maplength
    # Adjusted format string to match the number of provided integers
    header = struct.pack('>IIIIIIII', MAGIC_NUMBER, width, height, depth, width * height * (depth // 8), ras_type, maptype, maplength)
    return header

def generate_ras_image(file_path, width, height, color=(255, 0, 0)):
    """
    Generates a simple .ras image with a solid color.
    
    Parameters:
    - file_path: Path to save the .ras file.
    - width: Width of the image.
    - height: Height of the image.
    - color: A tuple (R, G, B) specifying the color.
    """
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Create a numpy array with the specified color
    data = np.zeros((height, width, 3), dtype=np.uint8)
    data[:] = color
    
    # Flatten the array to a bytes object
    pixel_data = data.tobytes()
    
    # Create and write the header
    header = create_ras_header(width, height)
    
    with open(file_path, 'wb') as file:
        file.write(header)
        file.write(pixel_data)
    
    print(f'Image saved as {file_path}')

# Example usage
generate_ras_image('./tmp/generated_image.ras', 640, 480, color=(255, 0, 0))