from PIL import Image
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image
img = Image.new('RGB', (100, 100), color = 'red')

# Dummy ICC profile data (normally you would load this from a valid ICC profile file)
# This is just placeholder data for demonstration
icc_profile_data = b'\x00' * 3144  # A minimal, non-functional ICC profile placeholder

# Save the image with the ICC profile
img.save('./tmp/colormanaged_image.jpg', 'JPEG', icc_profile=icc_profile_data)

print("Image with ICC profile saved.")