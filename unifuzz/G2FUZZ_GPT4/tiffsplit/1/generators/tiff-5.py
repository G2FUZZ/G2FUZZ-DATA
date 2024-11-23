import numpy as np
import tifffile as tiff
import os

# Create a directory for saving the generated TIFF files if it doesn't exist
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Generate an image with an alpha channel
# For demonstration, let's create a 100x100 image with 4 channels (RGBA)
width, height = 100, 100
channels = 4  # RGBA, where A is the alpha channel

# Create an array filled with random values for RGB and set the alpha channel to a specific value (e.g., 128 for 50% transparency)
image_data = np.random.randint(0, 256, (height, width, channels), dtype=np.uint8)
image_data[:, :, 3] = 128  # Set the alpha channel to 128 (50% transparency)

# Save the image as a TIFF file with an alpha channel
tiff_filename = os.path.join(output_dir, "image_with_alpha.tiff")
tiff.imwrite(tiff_filename, image_data)

print(f"TIFF file with alpha channel saved to {tiff_filename}")