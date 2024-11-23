from PIL import Image, ImageCms
import os

# Ensure the tmp directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Create a simple image
img = Image.new('RGB', (100, 100), color = 'blue')

# Load a standard sRGB ICC profile
icc_profile = ImageCms.createProfile("sRGB")

# Convert PIL image to have the ICC profile embedded
# Note: The output image should already have the ICC profile embedded
output_img = ImageCms.profileToProfile(img, icc_profile, icc_profile, outputMode='RGB')

# Save the image
output_path = os.path.join(output_dir, 'image_with_icc.tiff')
output_img.save(output_path, format='TIFF')

print(f"Image saved to {output_path}")