import numpy as np

def create_tga_file_with_color_map(file_path, width, height):
    # Define color map
    color_map = np.random.randint(0, 256, size=(256, 3), dtype=np.uint8)
    
    # Create TGA image data
    image_data = np.random.randint(0, 256, size=(height, width), dtype=np.uint8)
    
    # Write TGA file
    with open(file_path, 'wb') as f:
        # Write header (omitted for simplicity)
        
        # Write color map
        for color in color_map.flatten():
            f.write(int(color).to_bytes(1, byteorder='little'))
        
        # Write image data (omitted for simplicity)

# Generate TGA file with color map
file_path = './tmp/color_map_example.tga'
width = 100
height = 100
create_tga_file_with_color_map(file_path, width, height)