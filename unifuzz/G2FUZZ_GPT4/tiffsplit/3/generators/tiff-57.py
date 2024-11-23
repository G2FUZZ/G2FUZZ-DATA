from PIL import Image
import numpy as np
import os

# Create the tmp directory if it doesn't exist
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to generate a multi-page, multi-channel pyramidal TIFF
def generate_complex_tiff(filename, base_resolution=(1024, 1024), num_channels=3, num_pages=5):
    for page in range(num_pages):
        # Generate a base image for each channel
        channel_images = []
        for channel in range(num_channels):
            base_image = np.random.rand(*base_resolution) * 255
            base_pil_image = Image.fromarray(base_image.astype('uint8')).convert("L")

            # Create a list to hold the images for different resolutions for this channel
            resolutions = [2**i for i in range(4)]  # Example: 1/2, 1/4, 1/8, 1/16 of the base resolution
            images = []

            for res in resolutions:
                # Resize the base image to create a lower resolution version for this channel
                new_size = (base_resolution[0] // res, base_resolution[1] // res)
                resized_image = base_pil_image.resize(new_size, Image.Resampling.LANCZOS)
                images.append(resized_image)

            # Append images in reverse order to start with the highest resolution for this channel
            if channel == 0:
                # For the first channel, we need to save the image normally
                images[0].save(filename, save_all=True, append_images=images[1:][::-1], compression="tiff_deflate")
            else:
                # For subsequent channels, append to the existing file
                images[0].save(filename, save_all=True, append_images=images[1:][::-1], compression="tiff_deflate", append=True)

# Generate and save a complex TIFF
generate_complex_tiff(os.path.join(output_dir, "complex_tiff_example.tif"))