import numpy as np

def create_tga_file(color_depth, file_name):
    if color_depth == '8-bit grayscale':
        image = np.random.randint(0, 256, size=(100, 100), dtype=np.uint8)
    elif color_depth == '16-bit grayscale':
        image = np.random.randint(0, 65536, size=(100, 100), dtype=np.uint16)
    elif color_depth == '24-bit RGB':
        image = np.random.randint(0, 256, size=(100, 100, 3), dtype=np.uint8)
    elif color_depth == '32-bit RGBA':
        image = np.random.randint(0, 256, size=(100, 100, 4), dtype=np.uint8)
    else:
        raise ValueError('Invalid color depth specified')

    with open(f'./tmp/{file_name}.tga', 'wb') as f:
        f.write(b'\x00' * 18)  # TGA header
        f.write(image.tobytes())

# Create TGA files with different color depths
create_tga_file('8-bit grayscale', 'image_8bit')
create_tga_file('16-bit grayscale', 'image_16bit')
create_tga_file('24-bit RGB', 'image_24bit')
create_tga_file('32-bit RGBA', 'image_32bit')