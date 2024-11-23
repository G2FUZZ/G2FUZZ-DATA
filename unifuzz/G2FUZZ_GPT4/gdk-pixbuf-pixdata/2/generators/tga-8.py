import os

def create_tga(filename, width, height, pixel_depth, origin):
    """
    Create a TGA file with specified width, height, pixel depth, and origin.
    Origin: 0 for bottom-left, 1 for top-left.
    """
    header = bytearray(18)
    # Set image dimensions
    header[12:14] = width.to_bytes(2, byteorder='little')
    header[14:16] = height.to_bytes(2, byteorder='little')
    # Set image pixel depth
    header[16] = pixel_depth
    # Set image descriptor byte for origin (bit 5)
    header[17] = origin << 5

    # Generate image data: simple gradient
    data = bytearray()
    for y in range(height):
        for x in range(width):
            # Simple gradient effect based on position
            blue = x % 256
            green = y % 256
            red = (x + y) % 256
            # Append pixel data
            data.extend([blue, green, red])

    # Write to file
    with open(filename, 'wb') as f:
        f.write(header)
        f.write(data)

def main():
    # Ensure tmp directory exists
    os.makedirs('./tmp/', exist_ok=True)

    # Image parameters
    width, height, pixel_depth = 100, 100, 24  # 24 bits: 8 bits per channel (RGB)

    # Create TGA file with origin at bottom-left
    create_tga('./tmp/bottom_left_origin.tga', width, height, pixel_depth, 0)
    # Create TGA file with origin at top-left
    create_tga('./tmp/top_left_origin.tga', width, height, pixel_depth, 1)

if __name__ == "__main__":
    main()