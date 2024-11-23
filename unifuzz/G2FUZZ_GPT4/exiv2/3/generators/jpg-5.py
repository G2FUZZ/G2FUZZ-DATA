import os
from PIL import Image

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Create a base image (full-size)
base_image = Image.new('RGB', (800, 600), 'blue')

# Create a thumbnail (smaller version)
thumbnail_size = (80, 60)
thumbnail_image = base_image.copy()
thumbnail_image.thumbnail(thumbnail_size)

# Embed the thumbnail into the original image's info dictionary
base_image.info['thumbnail'] = thumbnail_image

# Save the image with the embedded thumbnail
output_path = os.path.join(output_dir, 'image_with_thumbnail.jpg')
base_image.save(output_path, 'JPEG')

print(f"Image saved with an embedded thumbnail at: {output_path}")