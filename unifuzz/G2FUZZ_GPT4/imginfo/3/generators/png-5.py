import numpy as np
import os
from PIL import Image

def apply_gamma_correction(image_array, gamma):
    """
    Apply gamma correction to an image array.
    :param image_array: numpy array of the image
    :param gamma: float, the gamma correction value
    :return: numpy array with gamma correction applied
    """
    # Normalize the pixel values to 0-1
    normalized_array = image_array / 255.0
    # Apply gamma correction
    corrected_array = np.power(normalized_array, gamma)
    # Convert back to 0-255 range
    corrected_image = np.uint8(corrected_array * 255)
    return corrected_image

def create_gamma_corrected_image(output_path, gamma=2.2):
    """
    Creates a gamma-corrected PNG image.
    :param output_path: string, path to save the image
    :param gamma: float, the gamma correction value
    """
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Create an example image (gradient)
    width, height = 256, 256
    image_array = np.zeros((height, width, 3), dtype=np.uint8)
    for i in range(width):
        for j in range(height):
            image_array[j, i] = [i, i, i]  # Creating a gradient

    # Apply gamma correction
    gamma_corrected_image = apply_gamma_correction(image_array, gamma)

    # Save the image
    img = Image.fromarray(gamma_corrected_image, 'RGB')
    img.save(output_path, 'PNG')

# Example usage
create_gamma_corrected_image('./tmp/gamma_corrected_image.png', 2.2)