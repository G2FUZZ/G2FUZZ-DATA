import os

def create_bmp_file(file_path, width, height, color):
    """
    Create a simple BMP file without compression.

    Args:
    - file_path: The path to save the BMP file.
    - width: The width of the image.
    - height: The height of the image.
    - color: A tuple of (R, G, B) to fill the image.
    """
    header_size = 54  # BMP header size
    pixel_size = 3  # 3 bytes per pixel for RGB

    # BMP Header
    header = bytearray(header_size)
    
    # BMP file type (2 bytes)
    header[0:2] = b'BM'
    
    # File size (4 bytes)
    file_size = header_size + width * height * pixel_size
    header[2:6] = file_size.to_bytes(4, byteorder='little')
    
    # Pixel data offset (4 bytes)
    header[10:14] = (header_size).to_bytes(4, byteorder='little')
    
    # DIB Header size (4 bytes)
    header[14:18] = (40).to_bytes(4, byteorder='little')
    
    # Image width and height (4 bytes each)
    header[18:22] = width.to_bytes(4, byteorder='little')
    header[22:26] = height.to_bytes(4, byteorder='little')
    
    # Planes (2 bytes)
    header[26:28] = (1).to_bytes(2, byteorder='little')
    
    # Bits per pixel (2 bytes)
    header[28:30] = (24).to_bytes(2, byteorder='little')
    
    # BI_RGB, no compression (4 bytes)
    header[30:34] = (0).to_bytes(4, byteorder='little')

    # Image data
    image_data = bytearray()
    for _ in range(height):
        for _ in range(width):
            image_data += bytearray(color)
        # Padding for 4-byte alignment
        padding = (4 - (width * pixel_size % 4)) % 4
        image_data += bytearray(padding)
    
    # Combine header and image data
    bmp_data = header + image_data

    # Save to file
    with open(file_path, 'wb') as f:
        f.write(bmp_data)

# Example usage
os.makedirs('./tmp/', exist_ok=True)
create_bmp_file('./tmp/uncompressed_image.bmp', 100, 100, (255, 0, 0))  # Red image