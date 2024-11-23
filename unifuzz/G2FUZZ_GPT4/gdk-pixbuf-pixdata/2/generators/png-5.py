import os
import numpy as np
from PIL import Image

def apply_gamma_correction(image, gamma):
    """
    Applies gamma correction to an image.

    Parameters:
        image (PIL.Image): The input image.
        gamma (float): The gamma correction value.

    Returns:
        PIL.Image: The gamma-corrected image.
    """
    # Convert to float and scale between 0 and 1
    img_float = np.array(image).astype(np.float32) / 255.0
    
    # Apply gamma correction
    corrected_img = np.power(img_float, gamma)
    
    # Convert back to an 8-bit format
    corrected_img = np.uint8(corrected_img * 255)
    
    # Return the corrected image
    return Image.fromarray(corrected_img)

def create_gamma_corrected_image(output_path, gamma=2.2, size=(256, 256), color=(255, 0, 0)):
    """
    Creates a simple image and applies gamma correction to it.

    Parameters:
        output_path (str): The path where the gamma-corrected image will be saved.
        gamma (float): The gamma correction value.
        size (tuple): The size of the image.
        color (tuple): The color of the image in RGB format.
    """
    # Create a base image
    img = Image.new('RGB', size, color=color)
    
    # Apply gamma correction
    corrected_img = apply_gamma_correction(img, gamma)
    
    # Save the corrected image
    corrected_img.save(output_path)

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate and save the gamma-corrected image
gamma_value = 2.2  # Example gamma value
output_file = './tmp/gamma_corrected_image.png'
create_gamma_corrected_image(output_file, gamma=gamma_value)

print(f"Gamma-corrected image saved to {output_file}")