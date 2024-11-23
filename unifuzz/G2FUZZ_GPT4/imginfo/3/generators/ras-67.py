import os
import struct

def create_ras_file(filename, width, height, depth, use_rle=False, use_colormap=False):
    # Sun Raster file magic number
    magic_number = 0x59a66a95
    # Header values
    type = 1 if use_rle else 0  # 1 for RLE compressed
    maptype = 1 if use_colormap else 0  # 1 for RGB colormap
    maplength = 768 if use_colormap and depth == 8 else 0  # 256 * 3 for RGB
    
    # Simulate image data
    if use_rle:
        # For simplicity, assume a repeating pattern that can be compressed
        # This is a placeholder for actual RLE compression logic
        image_data = b'\x01\xFF' * (width * height // 2)
    else:
        # Generate dummy image data (random or patterned)
        image_data = bytes([i % 256 for i in range(width * height * (depth // 8))])
    
    # Calculate length of the image data
    length = len(image_data)
    
    # Generate colormap (if applicable)
    colormap = bytes()
    if use_colormap and depth == 8:
        # Simple grayscale colormap, for example
        for i in range(256):
            colormap += struct.pack('BBB', i, i, i)  # Grayscale RGB
    
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # Open file to write binary data
    with open(f'./tmp/{filename}', 'wb') as file:
        # Write header information to the file
        file.write(struct.pack('>IIIIIIII', magic_number, width, height, depth, length, type, maptype, maplength))
        # Write colormap data (if any)
        if colormap:
            file.write(colormap)
        # Write the image data
        file.write(image_data)

# Example usage with colormap and no compression
create_ras_file('example_colormap.ras', 640, 480, 8, use_rle=False, use_colormap=True)

# Example usage with RLE compression
create_ras_file('example_rle.ras', 640, 480, 24, use_rle=True, use_colormap=False)