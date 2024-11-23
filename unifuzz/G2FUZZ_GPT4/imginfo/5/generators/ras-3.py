import os
import struct

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def create_ras_file(filename, width, height, data, compression=1):
    """
    Create a .ras file with the specified parameters.
    
    Args:
    - filename (str): The name of the file to save.
    - width (int): The width of the image.
    - height (int): The height of the image.
    - data (bytes): The pixel data.
    - compression (int): 1 for RLE compression, 0 for no compression.
    """
    # RAS file header format
    # magic (4 bytes), width (4 bytes), height (4 bytes),
    # depth (4 bytes), length (4 bytes), type (4 bytes),
    # maptype (4 bytes), maplength (4 bytes)
    magic = 0x59a66a95  # Magic number for RAS files
    depth = 24  # Assuming 24-bit color depth
    length = len(data)  # Length of the image data
    maptype = 0  # Colormap type, 0 for no colormap
    maplength = 0  # Length of the colormap
    
    # Construct the file header
    header = struct.pack('>IIIIIIII', magic, width, height, depth, length, compression, maptype, maplength)
    
    # Write the file
    with open(filename, 'wb') as f:
        f.write(header)
        f.write(data)

def create_dummy_image_data(width, height):
    """
    Create dummy image data for demonstration purposes.
    
    Args:
    - width (int): The width of the image.
    - height (int): The height of the image.
    
    Returns:
    - bytes: The generated image data.
    """
    # Generating a simple pattern: alternating red and green pixels
    # Red: 0xFF0000, Green: 0x00FF00
    data = bytearray()
    for y in range(height):
        for x in range(width):
            if (x + y) % 2 == 0:
                data.extend(b'\xFF\x00\x00')  # Red
            else:
                data.extend(b'\x00\xFF\x00')  # Green
    return bytes(data)

# Example usage
width, height = 100, 100  # Example dimensions
data = create_dummy_image_data(width, height)
filename = './tmp/example.ras'
create_ras_file(filename, width, height, data, compression=1)  # Using RLE compression