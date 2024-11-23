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

# Create base images for stereo effect
base_image_left = create_sample_image(2048, 2048, (255, 0, 0))
base_image_right = create_sample_image(2048, 2048, (0, 0, 255))

# Convert the PIL images to NumPy arrays for manipulation
base_array_left = np.array(base_image_left)
base_array_right = np.array(base_image_right)

# Define lists to hold the pyramidal layers (different resolutions) for both images
pyramid_left = [base_array_left]
pyramid_right = [base_array_right]

# Generate lower resolution layers for the pyramid of both images
for i in range(1, 5):  # Creating 4 additional layers for each image
    factor = 2 ** i
    # Reduce the resolution by downscaling for both images
    reduced_image_left = base_image_left.resize((2048 // factor, 2048 // factor), Image.Resampling.LANCZOS)
    reduced_image_right = base_image_right.resize((2048 // factor, 2048 // factor), Image.Resampling.LANCZOS)
    
    pyramid_left.append(np.array(reduced_image_left))
    pyramid_right.append(np.array(reduced_image_right))

# Save the pyramid as a TIFF with pyramidal layers and stereo image support
with TiffWriter('./tmp/stereo_pyramidal_image.tif', bigtiff=True) as tiff:
    for i in range(len(pyramid_left)):
        # Write the left image layer
        tiff.write(pyramid_left[i], subfiletype=1 if i > 0 else 0, metadata={'axes': 'YX'})
        # Write the right image layer immediately after the left image layer to form a stereo pair
        tiff.write(pyramid_right[i], subfiletype=3 if i == 0 else 2, metadata={'axes': 'YX'})

print("Stereo Pyramidal TIFF image has been saved.")