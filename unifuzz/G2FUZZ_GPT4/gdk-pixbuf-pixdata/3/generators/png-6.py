from PIL import Image
import numpy as np
import os

def apply_gamma_correction(image, gamma):
    """
    Apply gamma correction to an image.
    :param image: PIL Image object.
    :param gamma: Gamma value.
    :return: Gamma corrected PIL Image object.
    """
    inv_gamma = 1.0 / gamma
    table = [((i / 255.0) ** inv_gamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)
    return Image.fromarray(np.array(image).astype(np.uint8)).point(table)

def create_gamma_image(width, height, gamma):
    """
    Create a gradient image with gamma correction.
    :param width: Width of the image.
    :param height: Height of the image.
    :param gamma: Gamma value for correction.
    :return: Gamma corrected PIL Image object.
    """
    # Create a gradient from black to white
    gradient = np.linspace(0, 255, width, dtype=np.uint8)
    gradient = np.tile(gradient, (height, 1))

    # Convert to PIL Image
    image = Image.fromarray(gradient)

    # Apply gamma correction
    gamma_corrected = apply_gamma_correction(image, gamma)
    
    return gamma_corrected

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create and save the image with gamma correction
width, height = 800, 100  # Image dimensions
gamma_values = [0.5, 1.0, 2.2]  # Common gamma values

for gamma in gamma_values:
    image = create_gamma_image(width, height, gamma)
    image.save(f'./tmp/gamma_corrected_{gamma}.png')

print("Images have been generated and saved in './tmp/'.")