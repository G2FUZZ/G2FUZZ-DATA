import numpy as np
import os

def create_bmp_file(color_depth, file_path):
    if color_depth == 1:
        image = np.random.randint(0, 2, size=(100, 100)) * 255  # 1-bit monochrome
    elif color_depth == 8:
        image = np.random.randint(0, 256, size=(100, 100))  # 8-bit grayscale
    elif color_depth == 24:
        image = np.random.randint(0, 256, size=(100, 100, 3))  # 24-bit true color
    elif color_depth == 32:
        image = np.random.randint(0, 256, size=(100, 100, 4))  # 32-bit with alpha channel
    else:
        print("Unsupported color depth.")
        return
    
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))
    
    if color_depth == 1 or color_depth == 8:
        image = np.repeat(np.expand_dims(image, axis=2), 3, axis=2)  # Convert to 3 channels for visualization
    
    image = image.astype(np.uint8)
    if color_depth == 32:
        image[:, :, 3] = np.random.randint(0, 256, size=(100, 100))  # Random alpha channel values for 32-bit
    
    with open(file_path, 'wb') as f:
        if color_depth == 1:
            f.write(b'BM')
            f.write((54 + 2 ** 8).to_bytes(4, byteorder='little'))
            f.write((0).to_bytes(2, byteorder='little'))
            f.write((0).to_bytes(2, byteorder='little'))
            f.write((54).to_bytes(4, byteorder='little'))
            f.write((40).to_bytes(4, byteorder='little'))
            f.write((100).to_bytes(4, byteorder='little'))
            f.write((100).to_bytes(4, byteorder='little'))
            f.write((1).to_bytes(2, byteorder='little'))
            f.write((8).to_bytes(2, byteorder='little'))
            f.write((0).to_bytes(4, byteorder='little'))
            f.write((2 ** 8).to_bytes(4, byteorder='little'))
            f.write((2 ** 8).to_bytes(4, byteorder='little'))
            f.write((0).to_bytes(4, byteorder='little'))
            f.write((0).to_bytes(4, byteorder='little'))
            f.write(image.tobytes())
        else:
            if color_depth == 8:
                color_table = np.stack((np.arange(256),) * 3, axis=-1).astype(np.uint8)
                f.write(b'BM')
                f.write((54 + 256 * 3).to_bytes(4, byteorder='little'))
                f.write((0).to_bytes(2, byteorder='little'))
                f.write((0).to_bytes(2, byteorder='little'))
                f.write((54 + 256 * 3).to_bytes(4, byteorder='little'))
                f.write((40).to_bytes(4, byteorder='little'))
                f.write((100).to_bytes(4, byteorder='little'))
                f.write((100).to_bytes(4, byteorder='little'))
                f.write((1).to_bytes(2, byteorder='little'))
                f.write((8).to_bytes(2, byteorder='little'))
                f.write((0).to_bytes(4, byteorder='little'))
                f.write((256).to_bytes(4, byteorder='little'))
                f.write((256).to_bytes(4, byteorder='little'))
                f.write((0).to_bytes(4, byteorder='little'))
                f.write((0).to_bytes(4, byteorder='little'))
                f.write(color_table.tobytes())
                f.write(image.tobytes())
            else:
                f.write(b'BM')
                f.write((54 + image.size).to_bytes(4, byteorder='little'))
                f.write((0).to_bytes(2, byteorder='little'))
                f.write((0).to_bytes(2, byteorder='little'))
                f.write((54).to_bytes(4, byteorder='little'))
                f.write((40).to_bytes(4, byteorder='little'))
                f.write((100).to_bytes(4, byteorder='little'))
                f.write((100).to_bytes(4, byteorder='little'))
                f.write((1).to_bytes(2, byteorder='little'))
                f.write((color_depth).to_bytes(2, byteorder='little'))
                f.write((0).to_bytes(4, byteorder='little'))
                f.write((0).to_bytes(4, byteorder='little'))
                f.write((0).to_bytes(4, byteorder='little'))
                f.write((0).to_bytes(4, byteorder='little'))
                f.write(image.tobytes())

# Create BMP files with different color depths
create_bmp_file(1, './tmp/1bit_monochrome.bmp')
create_bmp_file(8, './tmp/8bit_grayscale.bmp')
create_bmp_file(24, './tmp/24bit_true_color.bmp')
create_bmp_file(32, './tmp/32bit_alpha_channel.bmp')