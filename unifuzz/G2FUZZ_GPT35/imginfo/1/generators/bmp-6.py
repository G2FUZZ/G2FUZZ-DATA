import numpy as np
import os

# Function to create a BMP file with a color palette
def create_bmp_with_palette(filename, width, height, palette):
    # Create a numpy array representing the image
    image = np.zeros((height, width), dtype=np.uint8)
    
    # Assign colors from the palette to the image
    for i in range(height):
        for j in range(width):
            image[i, j] = palette[j % len(palette)]
    
    # Save the image as a BMP file
    with open(filename, 'wb') as f:
        # BMP File Header
        f.write(b'BM')  # Signature
        f.write((14 + 40 + 4 * len(palette) + height * width).to_bytes(4, byteorder='little'))  # File size
        f.write(b'\x00\x00\x00\x00')  # Reserved
        f.write((14 + 40 + 4 * len(palette)).to_bytes(4, byteorder='little'))  # Pixel data offset
        
        # BMP Info Header
        f.write((40).to_bytes(4, byteorder='little'))  # Info header size
        f.write(width.to_bytes(4, byteorder='little'))  # Width
        f.write(height.to_bytes(4, byteorder='little'))  # Height
        f.write((1).to_bytes(2, byteorder='little'))  # Planes
        f.write((8).to_bytes(2, byteorder='little'))  # Bits per pixel
        f.write(b'\x00\x00\x00\x00')  # Compression (None)
        f.write((height * width).to_bytes(4, byteorder='little'))  # Image size
        f.write(b'\x00\x00\x00\x00')  # X pixels per meter
        f.write(b'\x00\x00\x00\x00')  # Y pixels per meter
        f.write(len(palette).to_bytes(4, byteorder='little'))  # Colors in palette
        f.write(b'\x00\x00\x00\x00')  # Important colors
        
        # Color Palette
        for color in palette:
            f.write(bytes([color, color, color, 0]))  # Blue, Green, Red, Reserved
        
        # Image Data
        for i in range(height):
            for j in range(width):
                f.write(bytes([image[i, j]]))
    
# Generate and save BMP file with color palette
palette = [0, 63, 127, 191, 255]  # Palette with 5 colors
filename = './tmp/palette.bmp'
create_bmp_with_palette(filename, 200, 200, palette)

print(f'BMP file with color palette saved as: {filename}')