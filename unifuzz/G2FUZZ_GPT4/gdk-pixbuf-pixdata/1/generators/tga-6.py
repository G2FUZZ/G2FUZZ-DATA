import os

def create_color_map_tga(filename, width, height, palette, data):
    # TGA Header for color mapped images
    # Header: idlength, colormaptype, datatypecode, colormaporigin, colormaplength, colormapdepth
    header = bytearray([0, 1, 1, 0, 0, len(palette), 24, 0, 0, 0, 0, width % 256, width // 256, height % 256, height // 256, 24, 0])
    
    # Convert the palette to the correct format (BGR)
    color_map = bytearray()
    for color in palette:
        b, g, r = color
        color_map.extend([b, g, r])
    
    # Convert the data indices to bytes
    image_data = bytearray(data)

    # Combine everything
    tga_data = header + color_map + image_data

    # Write to file
    with open(filename, 'wb') as file:
        file.write(tga_data)

# Ensure tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the palette (B, G, R)
palette = [
    (0, 0, 0),      # Black
    (0, 0, 255),    # Red
    (0, 255, 0),    # Green
    (255, 0, 0),    # Blue
    (255, 255, 255) # White
]

# Image data using palette indices
width, height = 5, 5
data = [
    0, 1, 2, 3, 4,
    1, 0, 1, 2, 3,
    2, 1, 0, 1, 2,
    3, 2, 1, 0, 1,
    4, 3, 2, 1, 0
]

# Create and save the TGA file
create_color_map_tga('./tmp/indexed_image.tga', width, height, palette, data)