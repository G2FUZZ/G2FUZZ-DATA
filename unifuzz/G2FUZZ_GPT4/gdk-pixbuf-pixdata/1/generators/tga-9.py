import os
import numpy as np

def create_tga_image(orientation='top-left'):
    # Define image properties
    width, height = 100, 100  # Image dimensions
    color = (0, 255, 0)  # Green, in BGR format because TGA uses BGR by default

    # Create an array filled with the color
    image_data = np.zeros((height, width, 3), dtype=np.uint8) + color

    # Define TGA header
    header = np.zeros(18, dtype=np.uint8)
    header[2] = 2  # Image type: uncompressed true-color image
    
    # Convert width and height to bytes and then to np.uint8 array before assigning
    width_bytes = np.frombuffer(width.to_bytes(2, byteorder='little', signed=False), dtype=np.uint8)
    height_bytes = np.frombuffer(height.to_bytes(2, byteorder='little', signed=False), dtype=np.uint8)
    
    header[12:14] = width_bytes
    header[14:16] = height_bytes
    
    header[16] = 24  # Bits per pixel

    if orientation == 'bottom-left':
        header[17] = 0x00  # Image descriptor byte (bit 5 is 0 indicating bottom-left origin)
    else:  # 'top-left'
        header[17] = 0x20  # Image descriptor byte (bit 5 is 1 indicating top-left origin)

    # Ensure the output directory exists
    os.makedirs('./tmp/', exist_ok=True)

    # Save the image
    filename = f'./tmp/image_{orientation}.tga'
    with open(filename, 'wb') as f:
        f.write(header)
        f.write(image_data.tobytes())

# Generate TGA files with different orientations
create_tga_image('top-left')
create_tga_image('bottom-left')