import numpy as np

def create_tga_file(file_path, width, height, image_data):
    header = bytearray([0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, width % 256, width // 256, height % 256, height // 256, 24, 0])
    with open(file_path, 'wb') as file:
        file.write(header)
        file.write(image_data)

# Generate True Color image data (random RGB values)
width = 100
height = 100
image_data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
image_data = image_data.tobytes()

# Create and save the TGA file
file_path = "./tmp/true_color_image.tga"
create_tga_file(file_path, width, height, image_data)