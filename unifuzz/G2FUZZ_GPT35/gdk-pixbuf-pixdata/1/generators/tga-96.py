import numpy as np

# Define the color image data (2x2 pixels)
image_data = np.array([
    [[255, 0, 0], [0, 255, 0]],
    [[0, 0, 255], [255, 255, 0]]
], dtype=np.uint8)

# Create a TGA file with color image data
def create_tga_file_with_image(file_name, image_data):
    with open(file_name, 'wb') as f:
        # Header of a TGA file with color image (18 bytes)
        header = bytearray([0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 8, 0])

        # Write the header to the file
        f.write(header)

        # Flatten the image data array
        image_data_flat = image_data.flatten()

        # Write the image data to the file
        f.write(image_data_flat.tobytes())

# Save the color image data in a TGA file
file_name = "./tmp/color_image.tga"
create_tga_file_with_image(file_name, image_data)

print(f"File '{file_name}' with color image data created successfully.")