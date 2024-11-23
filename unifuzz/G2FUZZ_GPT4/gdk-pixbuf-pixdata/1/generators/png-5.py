import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

def apply_gamma_correction(image, gamma):
    """
    Applies gamma correction to a given image.
    """
    # Normalize the pixel values to [0, 1]
    normalized_image = image / 255.0
    # Apply gamma correction
    corrected_image = np.power(normalized_image, gamma)
    # Scale back to [0, 255]
    corrected_image = (corrected_image * 255).astype(np.uint8)
    return corrected_image

def create_gamma_correction_image(width=400, height=200, gamma=2.2):
    """
    Creates an image to demonstrate gamma correction.
    """
    # Create a gradient image from black to white
    gradient = np.tile(np.linspace(0, 255, width // 2), (height, 1)).astype(np.uint8)
    
    # Create the left half of the image (without gamma correction)
    left_half = gradient
    
    # Create the right half of the image (with gamma correction)
    right_half = apply_gamma_correction(gradient, gamma)
    
    # Combine the two halves
    combined_image = np.concatenate((left_half, right_half), axis=1)
    
    # Convert to an image
    image = Image.fromarray(combined_image, 'L')  # 'L' mode for grayscale
    
    return image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create the gamma correction image
gamma_image = create_gamma_correction_image()

# Save the image
gamma_image.save('./tmp/gamma_correction_demo.png')

print("Gamma correction demo image saved.")