import os

def create_ras_file(file_name, width, height, pixel_depth, compression):
    """
    Creates a simple .ras file with basic header information.
    
    Parameters:
    - file_name (str): The name of the file to create.
    - width (int): The width of the image.
    - height (int): The height of the image.
    - pixel_depth (int): The pixel depth of the image.
    - compression (bool): Whether the image is compressed or not.
    """
    # Ensure the tmp directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # Define the path to save the file
    file_path = os.path.join('./tmp/', file_name)
    
    # RAS file header format:
    # magic number (4 bytes) | width (4 bytes) | height (4 bytes) | depth (4 bytes) | length (4 bytes)
    # type (4 bytes) | maptype (4 bytes) | maplength (4 bytes)
    # Note: This is a simplified version; some fields are set based on assumptions for demonstration purposes.
    
    magic_number = 0x59a66a95  # Magic number for Sun Raster files
    length = width * height * (pixel_depth // 8)  # Assuming uncompressed, no colormap
    type_ = 1 if compression else 0  # 1 for RLE compressed, 0 for standard
    maptype = 0  # Assuming no colormap
    maplength = 0  # No colormap
    
    # Open the file in binary write mode
    with open(file_path, 'wb') as file:
        # Write header information
        file.write(magic_number.to_bytes(4, byteorder='big'))
        file.write(width.to_bytes(4, byteorder='big'))
        file.write(height.to_bytes(4, byteorder='big'))
        file.write(pixel_depth.to_bytes(4, byteorder='big'))
        file.write(length.to_bytes(4, byteorder='big'))
        file.write(type_.to_bytes(4, byteorder='big'))
        file.write(maptype.to_bytes(4, byteorder='big'))
        file.write(maplength.to_bytes(4, byteorder='big'))
        
        # For simplicity, fill the image data with zeros (representing a black image)
        image_data = bytearray([0] * length)
        file.write(image_data)

# Example usage
create_ras_file('example.ras', 100, 100, 24, False)