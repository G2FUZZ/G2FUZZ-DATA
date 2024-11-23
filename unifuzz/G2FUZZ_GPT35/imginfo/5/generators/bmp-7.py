import numpy as np
import os

def create_bmp_file(color_depth, file_path):
    if color_depth not in [1, 4, 8, 24]:
        print("Color depth not supported.")
        return
    
    if color_depth == 1:
        image_data = np.random.randint(0, 2, size=(100, 100), dtype=np.uint8) * 255
    elif color_depth == 4:
        image_data = np.random.randint(0, 16, size=(100, 100), dtype=np.uint8) * 16
    elif color_depth == 8:
        image_data = np.random.randint(0, 256, size=(100, 100), dtype=np.uint8)
    elif color_depth == 24:
        image_data = np.random.randint(0, 256, size=(100, 100, 3), dtype=np.uint8)
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    if color_depth == 24:
        from PIL import Image
        img = Image.fromarray(image_data, 'RGB')
        img.save(file_path)
    else:
        with open(file_path, 'wb') as f:
            f.write(b'BM')
            f.write((54 + 2 ** color_depth * 4).to_bytes(4, byteorder='little'))
            f.write(b'\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00')
            f.write((100).to_bytes(4, byteorder='little'))
            f.write((100).to_bytes(4, byteorder='little'))
            f.write(b'\x01\x00')
            f.write((2 ** color_depth).to_bytes(2, byteorder='little'))
            f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
            if color_depth == 1:
                for i in range(8):
                    f.write((0xFF).to_bytes(1, byteorder='little'))
            elif color_depth == 4:
                for i in range(64):
                    f.write((i * 17).to_bytes(1, byteorder='little'))
            elif color_depth == 8:
                for i in range(256):
                    f.write(i.to_bytes(1, byteorder='little'))
            for row in image_data:
                f.write(row.tobytes())
    
    print(f"BMP file with color depth {color_depth} created at {file_path}")

color_depth = 24  # Specify the color depth here
file_path = './tmp/test.bmp'  # Specify the file path here
create_bmp_file(color_depth, file_path)