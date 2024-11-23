from PIL import Image, ImageCms
import numpy as np
import os

# Ensure ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image (100x100 pixels, with red color)
width, height = 100, 100
image = Image.new("RGB", (width, height), "red")

# Load a standard sRGB profile
srgb_profile = ImageCms.createProfile("sRGB")

# Convert the PIL image to include the ICC profile
output_with_profile = ImageCms.profileToProfile(image, srgb_profile, srgb_profile)

# Save the image with ICC profile embedded
output_with_profile.save('./tmp/embedded_icc_profile.tiff', 'TIFF', compression='tiff_lzw')