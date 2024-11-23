import numpy as np
from PIL import Image
import os

def create_directory_structure(base_path, subdirectories):
    """
    Create a directory structure based on the provided base path and subdirectories.
    """
    for subdir in subdirectories:
        dir_path = os.path.join(base_path, subdir)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

def generate_random_image(width, height):
    """
    Generate a random image using numpy.
    """
    return np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

def save_image(image_array, path):
    """
    Save an image array to a specified path.
    """
    image = Image.fromarray(image_array, 'RGB')
    image.save(path)

def get_dominant_color_channel(image_array):
    """
    Determine the dominant color channel of the image.
    """
    sums = image_array.sum(axis=(0, 1))
    return np.argmax(sums)  # Returns 0 for Red, 1 for Green, 2 for Blue

def main():
    base_path = './tmp/complex_structure/'
    subdirectories = ['Red_dominant', 'Green_dominant', 'Blue_dominant']
    create_directory_structure(base_path, subdirectories)

    num_images = 10  # Number of images to generate
    width, height = 800, 600

    for i in range(num_images):
        image_array = generate_random_image(width, height)
        dominant_color = get_dominant_color_channel(image_array)

        # Map the dominant color to the corresponding folder
        color_map = {0: 'Red_dominant', 1: 'Green_dominant', 2: 'Blue_dominant'}
        folder_name = color_map[dominant_color]

        file_path = os.path.join(base_path, folder_name, f'random_image_{i}.jpg')
        save_image(image_array, file_path)
        print(f"Image saved in '{file_path}'")

if __name__ == "__main__":
    main()