import struct
import os
import numpy as np

def create_ras_file(filename, width, height, depth, data_type, map_type=0, color_map=None):
    """
    Create a RAS file with specified metadata and save it to ./tmp/ directory.
    This version supports adding a color map for palette-based images.

    Parameters:
    - filename: Name of the file to be saved (string).
    - width: Width of the image in pixels (int).
    - height: Height of the image in pixels (int).
    - depth: Color depth in bits per pixel (int).
    - data_type: Type of raster data (int).
    - map_type: Type of color map (int).
    - color_map: Color map data if applicable (list of tuples).
    """
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # RAS file magic number (always 0x59a66a95)
    magic_number = 0x59a66a95

    # Prepare color map data if provided
    map_length = 0
    map_data = b''
    if color_map is not None and map_type != 0:
        # Assuming each color map entry is 3 bytes (RGB)
        map_length = len(color_map) * 3
        for color in color_map:
            map_data += struct.pack('BBB', *color)

    # Calculate the length of the image data
    length = width * height * (depth // 8)

    # Adjust image data length for palette-based images
    if data_type == 1 and map_type != 0:  # Assuming data_type 1 is for palette-based images
        length = width * height  # Each pixel references a palette index (1 byte per pixel)

    # RAS file header format: magic (4 bytes), width (4 bytes), height (4 bytes),
    # depth (4 bytes), length (4 bytes), type (4 bytes), maptype (4 bytes), maplength (4 bytes)
    header = struct.pack('>IIIIIIII', magic_number, width, height, depth, length, data_type, map_type, map_length)

    # Generate dummy image data based on data_type
    image_data = generate_dummy_image_data(width, height, depth, data_type, map_type)

    # Create the RAS file with the specified header and data
    with open(f'./tmp/{filename}', 'wb') as file:
        file.write(header)
        file.write(map_data)
        file.write(image_data)

def generate_dummy_image_data(width, height, depth, data_type, map_type):
    """
    Generate dummy image data based on the specified parameters.

    Parameters:
    - width: Width of the image in pixels (int).
    - height: Height of the image in pixels (int).
    - depth: Color depth in bits per pixel (int).
    - data_type: Type of raster data (int).
    - map_type: Type of color map (int).

    Returns:
    - image_data: Dummy image data (bytes).
    """
    if data_type == 1 and map_type != 0:  # Palette-based image
        # Generating random indices for the color map
        image_data = np.random.randint(0, 256, width * height, dtype=np.uint8)
    else:  # Standard RGB or grayscale image
        num_channels = depth // 8
        image_data = np.random.randint(0, 256, width * height * num_channels, dtype=np.uint8)
    
    return image_data.tobytes()

# Example of creating a standard RGB RAS file
create_ras_file('standard_rgb.ras', 800, 600, 24, 1)

# Example of creating a palette-based RAS file with a simple color map
color_map = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue
create_ras_file('palette_based.ras', 800, 600, 8, 1, map_type=1, color_map=color_map)