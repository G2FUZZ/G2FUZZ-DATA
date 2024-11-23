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

# Adding Spot Color Support
# For demonstration, we'll define a spot color in a separate layer/channel.
# Note: In actual applications, spot colors are specific inks used in printing. Here, we simulate this by adding an extra channel.
# Let's assume the spot color is represented in an additional channel as a specific shade of blue for demonstration purposes.
spot_color_channel = np.zeros((height, width), dtype=np.uint8) + 150  # A specific shade of blue
# Merge the spot color channel with the original image data
# Note: Real-world implementation would handle spot colors differently, depending on the printing process and software.
extended_image_data = np.dstack((image_data, spot_color_channel))

# Save the extended image as a TIFF file
extended_tiff_filename = os.path.join(output_dir, "image_with_spot_color_support.tiff")
tiff.imwrite(extended_tiff_filename, extended_image_data, photometric='RGB')

print(f"TIFF file with alpha channel saved to {tiff_filename}")
print(f"TIFF file with Spot Color Support saved to {extended_tiff_filename}")