import os
from PIL import Image, ImageCms

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image
img = Image.new('RGB', (100, 100), color = 'red')

# Use a built-in sRGB profile for demonstration
srgb_profile = ImageCms.createProfile("sRGB")

# Convert image to use the sRGB color profile (demonstration, effectively no-op)
img_srgb = ImageCms.profileToProfile(img, srgb_profile, srgb_profile, outputMode='RGB')

# Save the image
img_srgb.save('./tmp/img_srgb_profile.jpg')

print("Image with sRGB color profile saved successfully.")