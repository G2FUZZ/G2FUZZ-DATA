import os
import numpy as np
from PIL import Image
from tifffile import TiffWriter, imread, imwrite

# Creating a sample image for demonstration
def create_sample_image(width, height, color):
    """
    Create a simple image with a solid color.

    Args:
    - width (int): The width of the image.
    - height (int): The height of the image.
    - color (tuple): The color of the image (R, G, B).

    Returns:
    - image (PIL.Image.Image): The created image.
    """
    image = Image.new("RGB", (width, height), color=color)
    return image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a base image
base_image = create_sample_image(2048, 2048, (255, 0, 0))

# Convert the PIL image to a NumPy array for manipulation
base_array = np.array(base_image)

# Define a list to hold the pyramidal layers (different resolutions)
pyramid = [base_array]

# Generate lower resolution layers for the pyramid
for i in range(1, 5):  # Creating 4 additional layers
    factor = 2 ** i
    # Reduce the resolution by downscaling
    reduced_image = base_image.resize((2048 // factor, 2048 // factor), Image.Resampling.LANCZOS)
    pyramid.append(np.array(reduced_image))

# Save the pyramid as a TIFF with pyramidal layers
with TiffWriter('./tmp/pyramidal_image.tif', bigtiff=True) as tiff:
    for layer in pyramid:
        tiff.write(layer, subfiletype=1 if layer is not pyramid[0] else 0)

print("Pyramidal TIFF image has been saved.")