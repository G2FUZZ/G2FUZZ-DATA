import numpy as np
import os

def create_bmp_file(filename, width, height, color_depth):
    if color_depth not in [1, 4, 8, 16, 24, 32]:
        print("Unsupported color depth")
        return
    
    if not os.path.exists("./tmp"):
        os.makedirs("./tmp")
    
    if color_depth <= 8:
        dtype = np.uint8
    elif color_depth <= 16:
        dtype = np.uint16
    else:
        dtype = np.uint32
    
    image_data = np.random.randint(0, 2**color_depth, size=(height, width), dtype=dtype)
    image_data = np.repeat(image_data[:, :, np.newaxis], 3, axis=2)  # Create RGB image
    
    header = np.array([int.from_bytes(width.to_bytes(4, byteorder='little', signed=False), byteorder='little'),
                       int.from_bytes(height.to_bytes(4, byteorder='little', signed=False), byteorder='little'),
                       int.from_bytes((54).to_bytes(4, byteorder='little', signed=False), byteorder='little')], dtype=np.uint32)
    
    with open(f"./tmp/{filename}.bmp", "wb") as f:
        f.write(b'BM')
        f.write((54 + image_data.size * 3).to_bytes(4, byteorder='little', signed=False))
        f.write(header.tobytes())
        f.write(image_data.tobytes())

create_bmp_file("test_bmp_24bit", 100, 100, 24)