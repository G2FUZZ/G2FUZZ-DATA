import os

def create_tga_file(file_path, width, height, color_depth, use_rle=True, image_type='gradient'):
    """
    Generates a TGA file with options for RLE compression and different image types.
    
    Args:
    - file_path: Path to save the TGA file.
    - width: Width of the image.
    - height: Height of the image.
    - color_depth: Color depth (e.g., 24 for RGB).
    - use_rle: Whether to use RLE compression.
    - image_type: Type of image to generate ('blue' for a solid blue image, 'gradient' for a horizontal gradient).
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # TGA Header
    header = bytearray([
        0,  # ID length
        0,  # Color map type
        10 if use_rle else 2,  # Image type (10 for RLE compressed true-color image, 2 for uncompressed)
        0, 0, 0, 0, 0,  # Color map specification
        0, 0,  # X-origin
        0, 0,  # Y-origin
        width & 0xFF, (width >> 8) & 0xFF,  # Width
        height & 0xFF, (height >> 8) & 0xFF,  # Height
        color_depth,  # Pixel depth
        0  # Image descriptor
    ])
    
    # Generate pixel data based on the chosen image type
    if image_type == 'blue':
        pixel_data = bytearray([255, 0, 0] * width * height)
    elif image_type == 'gradient':
        pixel_data = bytearray()
        for i in range(height):
            for j in range(width):
                pixel_data += bytearray([
                    int((j / width) * 255),  # Blue gradient
                    0,  # Green channel
                    int((1 - (j / width)) * 255),  # Red gradient
                ])
    
    # Apply RLE compression if required
    if use_rle:
        compressed_data = rle_compress(pixel_data, color_depth // 8)
    else:
        compressed_data = pixel_data
    
    # Write the file
    with open(file_path, 'wb') as f:
        f.write(header)
        f.write(compressed_data)

def rle_compress(pixel_data, bytes_per_pixel):
    """
    Compresses pixel data using RLE.
    
    Args:
    - pixel_data: The raw pixel data to compress.
    - bytes_per_pixel: Number of bytes per pixel (3 for RGB, 4 for RGBA).
    
    Returns:
    - A bytearray of the compressed pixel data.
    """
    compressed_data = bytearray()
    current_pixel = pixel_data[:bytes_per_pixel]
    count = 1
    
    for i in range(bytes_per_pixel, len(pixel_data), bytes_per_pixel):
        new_pixel = pixel_data[i:i+bytes_per_pixel]
        if new_pixel == current_pixel and count < 128:
            count += 1
        else:
            compressed_data.append(0x80 | (count - 1))  # Signal that this is a run
            compressed_data += current_pixel
            current_pixel = new_pixel
            count = 1
    # Add the final pixel(s)
    compressed_data.append(0x80 | (count - 1))
    compressed_data += current_pixel
    
    return compressed_data

# Parameters for the image
width = 100  # Width of the image
height = 100  # Height of the image
color_depth = 24  # Color depth (24 for RGB)

# Generate and save the TGA file with RLE compression and a gradient
create_tga_file('./tmp/sample_rle_gradient.tga', width, height, color_depth, use_rle=True, image_type='gradient')