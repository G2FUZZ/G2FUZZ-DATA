import os
from PIL import Image

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)  # Fixed the variable name here

# Create a base image (full-size)
base_image = Image.new('RGB', (800, 600), 'blue')

# Create a thumbnail (smaller version)
thumbnail_size = (80, 60)
thumbnail_image = base_image.copy()
thumbnail_image.thumbnail(thumbnail_size)

# Embed the thumbnail into the original image's info dictionary
base_image.info['thumbnail'] = thumbnail_image

# Convert the base image to YCbCr color model
ycbcr_image = base_image.convert('YCbCr')

# Embed the Color Models feature description into the image's info dictionary
ycbcr_image.info['Color Models'] = "JPEG typically uses the YCbCr color model for color images, separating the image into a luminance component (Y) and two chrominance components (Cb and Cr) for efficient compression."

# Save the image with the embedded thumbnail and Color Models feature
output_path = os.path.join(output_dir, 'image_with_features.jpg')
ycbcr_image.save(output_path, 'JPEG')

print(f"Image saved with an embedded thumbnail and Color Models feature at: {output_path}")