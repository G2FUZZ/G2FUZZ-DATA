import os
from PIL import Image

# Create the tmp directory if it doesn't exist
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the size of the image
width, height = 100, 100

# Create a new image with RGB mode
image = Image.new("RGB", (width, height), "green")

# Normally, you would load an existing ICC profile from a file like so:
# with open("path_to_srgb_profile.icc", "rb") as f:
#     icc_profile = f.read()
# image.info['icc_profile'] = icc_profile

# Save the image (without explicitly setting an ICC profile in this simplified example)
output_file_path = os.path.join(output_dir, "pixdata_without_explicit_color_profile.jpg")
image.save(output_file_path)

print(f"Image saved at {output_file_path}")