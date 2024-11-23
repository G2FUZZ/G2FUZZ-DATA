import numpy as np

def create_tga_file(filename, image, color_map=None):
    width = image.shape[1]
    height = image.shape[0]
    
    # Define TGA header
    header = bytearray([0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    header += width.to_bytes(2, byteorder='little')
    header += height.to_bytes(2, byteorder='little')
    header += bytes([32])  # 32-bit color depth, 8 bits per channel
    
    if color_map is not None:
        header += bytes([1])  # Color-mapped image
        header += bytes([0])  # Origin of the color map
        header += color_map.tobytes()  # Color map data
    else:
        header += bytes([0])  # No color map
    
    # Save the image as a TGA file
    with open(filename, 'wb') as f:
        f.write(header)
        f.write(image.tobytes())

# Define image dimensions
width = 200
height = 200

# Create a color image
image = np.zeros((height, width, 4), dtype=np.uint8)
image[:, :width//2] = [255, 0, 0, 255]  # Red left side
image[:, width//2:] = [0, 0, 255, 255]  # Blue right side

# Define a color map (optional)
color_map = np.array([[255, 0, 0, 255],  # Red
                      [0, 0, 255, 255]])  # Blue

# Save the image as a TGA file with color map
create_tga_file('./tmp/color_image_with_map.tga', image, color_map)