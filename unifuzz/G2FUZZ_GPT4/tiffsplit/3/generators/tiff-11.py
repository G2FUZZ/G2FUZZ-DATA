from PIL import Image
import numpy as np
import os

# Create the tmp directory if it doesn't exist
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to generate a pyramidal TIFF
def generate_pyramidal_tiff(filename, base_resolution=(1024, 1024)):
    # Create a base image
    base_image = np.random.rand(*base_resolution, 3) * 255
    base_pil_image = Image.fromarray(base_image.astype('uint8')).convert("RGB")

    # Create a list to hold the images for different resolutions
    resolutions = [2**i for i in range(4)]  # Example: 1/2, 1/4, 1/8, 1/16 of the base resolution
    images = []

    for res in resolutions:
        # Resize the base image to create a lower resolution version
        new_size = (base_resolution[0] // res, base_resolution[1] // res)
        resized_image = base_pil_image.resize(new_size, Image.Resampling.LANCZOS)  # Updated to use Image.Resampling.LANCZOS
        images.append(resized_image)

    # Save the image as a pyramidal TIFF
    # Append images in reverse order to start with the highest resolution
    images[0].save(filename, save_all=True, append_images=images[1:][::-1], compression="tiff_deflate")

# Generate and save a pyramidal TIFF
generate_pyramidal_tiff(os.path.join(output_dir, "pyramidal_tiff_example.tif"))