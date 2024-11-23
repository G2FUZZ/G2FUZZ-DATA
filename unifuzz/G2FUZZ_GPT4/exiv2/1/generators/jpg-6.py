import os
from PIL import Image, ImageCms

# Create the tmp directory if it doesn't already exist
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image using PIL
size = (100, 100)  # Size of the image
color = (255, 0, 0)  # Red color
image = Image.new("RGB", size, color)

# Set up ICC profiles
# The sRGB profile is widely used and suitable for images on the web.
# Here, we're using a standard sRGB profile included with PIL for demonstration.
# In a real-world scenario, you might use a specific ICC profile that matches your needs.
srgb_profile = ImageCms.createProfile("sRGB")
icc_profile = ImageCms.getOpenProfile(srgb_profile)

# Save the image with an ICC profile embedded
output_file = './tmp/colored_with_icc_profile.jpg'
image.save(output_file, 'JPEG', icc_profile=icc_profile.tobytes())

print(f'Image saved to {output_file}')