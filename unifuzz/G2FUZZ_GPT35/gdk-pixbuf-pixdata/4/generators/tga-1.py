import numpy as np

# Create image data
image_data = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)

# Write image data to TGA file
def write_tga_file(image_data, file_path):
    header = bytearray([0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100 % 256, 100 // 256, 100 % 256, 100 // 256, 24, 32])
    with open(file_path, 'wb') as f:
        f.write(header)
        f.write(image_data)

# Save image data to TGA file
file_name = "./tmp/image.tga"
write_tga_file(image_data, file_name)