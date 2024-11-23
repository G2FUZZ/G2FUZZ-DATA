import os
from PIL import Image, ImageCms

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image
image = Image.new("RGB", (100, 100), color=(255, 0, 0))

# Path to save the image with embedded profile
image_path_with_profile = './tmp/image_with_profile.jpg'

# Use sRGB as an example profile. For real applications, use the accurate profile needed.
srgb_profile_path = ImageCms.createProfile("sRGB")

# Embed the sRGB profile into the image
ImageCms.profileToProfile(image, srgb_profile_path, srgb_profile_path, outputMode='RGB').save(image_path_with_profile, "JPEG", quality=95)

print(f"Image with embedded color profile saved at: {image_path_with_profile}")