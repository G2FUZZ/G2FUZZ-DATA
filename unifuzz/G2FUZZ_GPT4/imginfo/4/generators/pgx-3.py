import os
import numpy as np

def create_pgx_file(filename, width, height, data):
    """
    Creates a .pgx file with specified dimensions and data.

    :param filename: Name of the file to save (including path).
    :param width: Width of the image.
    :param height: Height of the image.
    :param data: A numpy array containing image data.
    """
    header = f"PG ML {width} {height} 255\n"  # PGX header for grayscale image, max value 255
    with open(filename, "wb") as file:
        file.write(header.encode('utf-8'))  # Write the header in UTF-8 encoding
        data.tofile(file)  # Write the image data

def generate_sample_image(width, height):
    """
    Generates a simple sample image as a numpy array.

    :param width: Width of the image.
    :param height: Height of the image.
    :return: A numpy array representing a grayscale image.
    """
    # Generate a simple gradient image for demonstration purposes
    img = np.zeros((height, width), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            img[y, x] = (x + y) % 256  # Simple pattern for visualization
    return img

# Define image dimensions
img_width = 256
img_height = 256

# Generate image data
image_data = generate_sample_image(img_width, img_height)

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# File path where the pgx file will be saved
file_path = './tmp/sample_image.pgx'

# Create the PGX file
create_pgx_file(file_path, img_width, img_height, image_data)

print(f"PGX file has been created at: {file_path}")