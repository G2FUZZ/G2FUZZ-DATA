import numpy as np
import pywt
import os
from PIL import Image

def apply_wavelet_transformation(image_array):
    """
    Apply wavelet transformation to an image array.
    """
    coeffs = pywt.dwt2(image_array, 'haar')
    cA, (cH, cV, cD) = coeffs
    return cA

def create_wavelet_transformed_image():
    # Create an example image (e.g., 256x256 pixels, grayscale)
    img_size = 256
    image = np.random.rand(img_size, img_size) * 255
    image = image.astype(np.uint8)

    # Apply wavelet transformation
    transformed_image = apply_wavelet_transformation(image)

    # Convert the transformed image back to an Image object
    # First, normalize the transformed image to the 0-255 range
    transformed_image = (transformed_image - transformed_image.min()) / (transformed_image.max() - transformed_image.min()) * 255
    # Then, convert to uint8
    transformed_image = transformed_image.astype(np.uint8)
    pil_img = Image.fromarray(transformed_image)

    # Ensure the './tmp/' directory exists
    os.makedirs('./tmp/', exist_ok=True)

    # Save the transformed image
    pil_img.save('./tmp/transformed_image.png')

create_wavelet_transformed_image()