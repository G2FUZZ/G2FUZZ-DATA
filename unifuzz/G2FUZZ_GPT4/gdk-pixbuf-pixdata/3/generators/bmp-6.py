import os
from PIL import Image

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an image
size = (100, 100)  # Size of the image
image = Image.new("RGB", size, color=(255, 0, 0))  # Create a red image

# Save the image without explicitly setting an ICC profile
# If you need to embed an ICC profile, consider using a format like JPEG or TIFF
output_path = './tmp/colored_image.jpg'
image.save(output_path, 'JPEG')

print(f"Image saved to {output_path}")