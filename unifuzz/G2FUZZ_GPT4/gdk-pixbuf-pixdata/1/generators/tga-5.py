import os

def create_tga_file(filename, width, height, color, alpha_flag):
    """
    Create a simple TGA file with a specified color and alpha channel flag.
    
    Args:
    - filename (str): The name of the file to save.
    - width (int): The width of the image.
    - height (int): The height of the image.
    - color (tuple): A tuple of 4 elements (R, G, B, A) defining the color and alpha.
    - alpha_flag (int): The flag indicating the use of the alpha channel (0-15).
    """
    # Ensure the tmp directory exists
    os.makedirs('./tmp', exist_ok=True)
    
    header = bytearray(18)  # TGA Header is 18 bytes
    # Set image specification
    header[2] = 2  # Truecolor image type
    header[12] = width & 0xFF
    header[13] = (width >> 8) & 0xFF
    header[14] = height & 0xFF
    header[15] = (height >> 8) & 0xFF
    header[16] = 32  # 32 bits per pixel
    header[17] = alpha_flag << 4 | 0x08  # Set alpha channel info and left-to-right order
    
    # Create the image data
    pixels = [color for _ in range(width * height)]
    
    # Flatten the list
    image_data = bytearray([item for sublist in pixels for item in sublist])
    
    # Combine header and image data
    tga_content = header + image_data
    
    # Write the file
    with open(f'./tmp/{filename}', 'wb') as file:
        file.write(tga_content)

# Example usage
create_tga_file('example.tga', 100, 100, (255, 0, 0, 128), 8)  # Red square with semi-transparent alpha