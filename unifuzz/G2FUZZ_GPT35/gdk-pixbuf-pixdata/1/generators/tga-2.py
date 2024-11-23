import numpy as np

def create_tga_file(color_depth, filename):
    if color_depth not in [16, 24, 32]:
        print("Unsupported color depth. Supported values are 16, 24, or 32.")
        return
    
    width, height = 100, 100
    if color_depth == 16:
        image_data = np.random.randint(0, 2**16, (height, width, 3), dtype=np.uint16)
    elif color_depth == 24:
        image_data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    else:  # color_depth == 32
        image_data = np.random.randint(0, 256, (height, width, 4), dtype=np.uint8)
    
    with open(f"./tmp/{filename}.tga", "wb") as f:
        # Write TGA header and image data here
        # This part would involve writing TGA file format specific data
        pass

# Generate TGA files with different color depths
create_tga_file(16, "tga_16bit")
create_tga_file(24, "tga_24bit")
create_tga_file(32, "tga_32bit")