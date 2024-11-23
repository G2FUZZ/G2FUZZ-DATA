import os
import struct

def create_color_map_tga(path, width, height, color_map, indexes):
    header = bytes([
        0,  # ID length
        1,  # Color map type (1 = has a color map)
        1,  # Image type (1 = color-mapped image)
        0, 0,  # First entry index (color map origin)
        len(color_map), 0,  # Color map length
        24,  # Color map depth (24 bits)
        0, 0,  # X-origin
        0, 0,  # Y-origin
        width & 0xFF, (width >> 8) & 0xFF,  # Width
        height & 0xFF, (height >> 8) & 0xFF,  # Height
        24,  # Pixel depth
        0,  # Image descriptor
    ])

    # Convert color map (RGB tuples) to bytes
    color_map_data = b''.join(struct.pack('BBB', *color) for color in color_map)

    # Convert indexes to bytes
    image_data = b''.join(struct.pack('B', idx) for idx in indexes)

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    # Write the file
    with open(path, 'wb') as f:
        f.write(header)
        f.write(color_map_data)
        f.write(image_data)

# Define a simple color map (palette)
color_map = [
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (255, 255, 0),  # Yellow
]

# Define indexes for a 4x1 image
indexes = [0, 1, 2, 3]

# Save the TGA file
create_color_map_tga('./tmp/palette_image.tga', 4, 1, color_map, indexes)