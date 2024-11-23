import os
import numpy as np

def generate_image_data(width, height, color_mode='solid', color=(0, 255, 0)):
    """
    Generate image data with different patterns based on the color_mode.
    """
    if color_mode == 'gradient':
        image_data = np.zeros((height, width, 3), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                image_data[y, x] = (x % 256, y % 256, (x + y) % 256)
    elif color_mode == 'solid':
        image_data = np.zeros((height, width, 3), dtype=np.uint8) + color
    else:
        raise ValueError("Unsupported color mode")
    return image_data

def rle_compress(image_data):
    """
    Compress the image data using RLE compression.
    """
    flat_pixels = image_data.flatten()
    compressed_data = []
    count = 1
    for i in range(1, len(flat_pixels)):
        if flat_pixels[i] == flat_pixels[i-1] and count < 128:
            count += 1
        else:
            compressed_data.append(count | 0x80)
            compressed_data.append(flat_pixels[i-1])
            count = 1
    compressed_data.append(count | 0x80)
    compressed_data.append(flat_pixels[-1])
    return np.array(compressed_data, dtype=np.uint8)

def create_tga_image(filename, width=100, height=100, color=(0, 255, 0), orientation='top-left', compression=False, color_mode='solid'):
    """
    Create and save a TGA image with specified properties.
    """
    # Generate image data
    image_data = generate_image_data(width, height, color_mode, color)

    # Define TGA header
    header = np.zeros(18, dtype=np.uint8)
    header[2] = 10 if compression else 2  # Image type: RLE true-color image (10) or uncompressed (2)
    
    width_bytes = np.frombuffer(width.to_bytes(2, byteorder='little', signed=False), dtype=np.uint8)
    height_bytes = np.frombuffer(height.to_bytes(2, byteorder='little', signed=False), dtype=np.uint8)
    
    header[12:14] = width_bytes
    header[14:16] = height_bytes
    
    header[16] = 24  # Bits per pixel

    if orientation == 'bottom-left':
        header[17] = 0x00  # Image descriptor byte for bottom-left origin
    else:  # 'top-left'
        header[17] = 0x20  # Image descriptor byte for top-left origin

    # Compress image data if necessary
    if compression:
        image_data = rle_compress(image_data)

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Save the image
    with open(filename, 'wb') as f:
        f.write(header)
        f.write(image_data.tobytes())

# Generate TGA files with different configurations
create_tga_image('./tmp/solid_uncompressed.tga', color_mode='solid', compression=False)
create_tga_image('./tmp/gradient_uncompressed.tga', color_mode='gradient', compression=False)
create_tga_image('./tmp/solid_compressed.tga', color_mode='solid', compression=True)
create_tga_image('./tmp/gradient_compressed.tga', color_mode='gradient', compression=True)