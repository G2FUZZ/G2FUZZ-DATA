import numpy as np

def generate_tga_file(image_data, width, height, color_depth=24, image_name='generated_image'):
    header = bytearray([0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, width % 256, width // 256, height % 256, height // 256, color_depth, 0])

    image_data_flattened = image_data.flatten()
    image_bytes = bytearray()

    for i in range(0, len(image_data_flattened), 3):
        # TGA is stored in BGR format
        image_bytes.append(image_data_flattened[i + 2])  # B
        image_bytes.append(image_data_flattened[i + 1])  # G
        image_bytes.append(image_data_flattened[i])      # R

    with open(f'./tmp/{image_name}.tga', 'wb') as file:
        file.write(header)
        file.write(image_bytes)

# Generate a sample image data
image_data = np.random.randint(0, 256, size=(200, 150, 3), dtype=np.uint8)

# Save the image data as a TGA file with custom features
generate_tga_file(image_data, width=200, height=150, color_depth=24, image_name='custom_image')