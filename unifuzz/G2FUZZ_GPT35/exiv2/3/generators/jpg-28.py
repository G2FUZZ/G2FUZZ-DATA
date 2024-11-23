import numpy as np
from PIL import Image
import os

# Create a random RGB image
def generate_random_image(width, height):
    image_data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    return Image.fromarray(image_data, 'RGB')

def batch_processing(input_folder, output_folder, new_width, new_height, compression_level):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):
            image_path = os.path.join(input_folder, filename)
            image = Image.open(image_path)
            resized_image = image.resize((new_width, new_height))
            output_path = os.path.join(output_folder, f'resized_{filename}')
            resized_image.save(output_path, quality=compression_level)

# Define parameters
width = 100
height = 100
compression_levels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
input_folder = './tmp/input_images'
output_folder = './tmp/output_images'
new_width = 50
new_height = 50

# Generate and save the original image
image = generate_random_image(width, height)
image.save(f'./tmp/generated_image.jpg', quality=5)

# Create the input_images directory if it does not exist
if not os.path.exists(input_folder):
    os.makedirs(input_folder)

# Perform batch processing on images in the input folder
batch_processing(input_folder, output_folder, new_width, new_height, 6)