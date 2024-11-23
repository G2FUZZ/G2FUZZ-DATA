import numpy as np

def create_tga_file(color_depth, filename):
    if color_depth not in [8, 16, 24, 32]:
        print("Invalid color depth. Supported values are 8, 16, 24, 32.")
        return

    width, height = 100, 100
    if color_depth == 8:
        image_data = np.random.randint(0, 256, (height, width), dtype=np.uint8)
    elif color_depth == 16:
        image_data = np.random.randint(0, 65536, (height, width), dtype=np.uint16)
    elif color_depth == 24:
        image_data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    elif color_depth == 32:
        image_data = np.random.randint(0, 256, (height, width, 4), dtype=np.uint8)

    with open(filename, 'wb') as f:
        f.write(b'\x00' * 18)  # TGA header
        f.write(image_data.tobytes())

# Save TGA files with different color depths
create_tga_file(8, './tmp/file_8bit.tga')
create_tga_file(16, './tmp/file_16bit.tga')
create_tga_file(24, './tmp/file_24bit.tga')
create_tga_file(32, './tmp/file_32bit.tga')