from PIL import Image, ImageCms
import os

# Directory to save the generated JPG
output_dir = './tmp/'

# Create a simple image - let's say a red square
img = Image.new('RGB', (100, 100), 'red')

# Load an ICC profile if it exists
icc_profile_path = 'sRGB_v4_ICC_preference.icc'
if os.path.exists(icc_profile_path):
    with open(icc_profile_path, 'rb') as f:
        icc_profile = f.read()
    # Apply the ICC profile to the image
    img.info['icc_profile'] = icc_profile
else:
    print(f"ICC profile {icc_profile_path} not found. Continuing without it.")

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save the image with the ICC profile embedded (if available)
img.save(os.path.join(output_dir, 'icc_profile_supported_image.jpg'), 'JPEG')

print("Image with ICC profile saved successfully.")