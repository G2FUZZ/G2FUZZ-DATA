import numpy as np
from PIL import Image
import os

def generate_gradient_image(width, height, pattern='vertical'):
    """
    Generate a gradient image based on the specified pattern.

    :param width: Width of the image
    :param height: Height of the image
    :param pattern: Pattern of the gradient ('vertical', 'horizontal', 'diagonal')
    :return: A numpy array representing the generated image
    """
    image = np.zeros((height, width, 3), dtype=np.uint8)
    
    if pattern == 'vertical':
        for y in range(height):
            r, g, b = y // 2, y // 3, y // 4
            image[y, :, 0] = r
            image[y, :, 1] = g
            image[y, :, 2] = b
    elif pattern == 'horizontal':
        for x in range(width):
            r, g, b = x // 2, x // 3, x // 4
            image[:, x, 0] = r
            image[:, x, 1] = g
            image[:, x, 2] = b
    elif pattern == 'diagonal':
        for y in range(height):
            for x in range(width):
                r, g, b = (x+y) // 2, (x+y) // 3, (x+y) // 4
                image[y, x, 0] = r
                image[y, x, 1] = g
                image[y, x, 2] = b
    else:
        raise ValueError("Unsupported pattern")

    return image

def save_image(image, path):
    """
    Save a numpy array as a jpg image.

    :param image: The numpy array to save as an image
    :param path: Path where the image will be saved
    """
    img = Image.fromarray(image, 'RGB')
    img.save(path, 'JPEG')

def create_complex_structure(width=800, height=600):
    """
    Create and save images with different gradient patterns in a structured directory.

    :param width: Width of the images
    :param height: Height of the images
    """
    patterns = ['vertical', 'horizontal', 'diagonal']
    base_dir = './tmp/complex_gradients/'

    # Ensure base directory exists
    os.makedirs(base_dir, exist_ok=True)

    for pattern in patterns:
        # Ensure a directory exists for this pattern
        pattern_dir = os.path.join(base_dir, pattern)
        os.makedirs(pattern_dir, exist_ok=True)

        image = generate_gradient_image(width, height, pattern)
        file_path = os.path.join(pattern_dir, f'{pattern}_gradient.jpg')
        save_image(image, file_path)
        print(f'Saved {file_path}')

create_complex_structure()