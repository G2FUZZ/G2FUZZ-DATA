import os
import struct

def create_colormap_tga():
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # Define the colormap (R, G, B): each color is 3 bytes
    # For simplicity, we're defining a colormap with 3 colors.
    colormap = [
        (255, 0, 0),  # Red
        (0, 255, 0),  # Green
        (0, 0, 255),  # Blue
    ]
    
    # Create an indexed image: each value is an index in the colormap
    width, height = 100, 100  # Image dimensions
    data = []
    for y in range(height):
        for x in range(width):
            # This example just cycles through the colormap indices
            index = (x + y) % len(colormap)
            data.append(index)
    
    # TGA Header for a colormap image
    header = struct.pack(
        "<BBBHHBHHHHBB",
        0,  # ID length
        1,  # Color map type (1 = has a colormap)
        1,  # Image type (1 = colormap image, uncompressed)
        0,  # First entry index (color map start)
        len(colormap),  # Color map length
        24,  # Color map depth (24 bits: 8 bits per channel)
        0, 0,  # X-origin, Y-origin
        width, height,  # Width, Height
        8,  # Pixel depth (8 bits: indexes into the colormap)
        0   # Image descriptor (attributes)
    )
    
    # Convert colormap and data to bytes
    colormap_bytes = b''.join(struct.pack('<BBB', *color) for color in colormap)
    data_bytes = bytes(data)
    
    # Write the TGA file
    with open('./tmp/colormap_example.tga', 'wb') as f:
        f.write(header)
        f.write(colormap_bytes)
        f.write(data_bytes)
    
    print("TGA file with colormap support has been created.")

create_colormap_tga()