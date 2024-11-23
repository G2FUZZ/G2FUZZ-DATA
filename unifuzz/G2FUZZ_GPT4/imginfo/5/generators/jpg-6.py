from PIL import Image, ImageOps
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a sample image (e.g., 800x600, blue background)
image = Image.new('RGB', (800, 600), color = (73, 109, 137))

# Create a thumbnail (e.g., 80x60)
thumbnail_size = (80, 60)
# Use Image.Resampling.LANCZOS instead of Image.ANTIALIAS
thumbnail = ImageOps.fit(image, thumbnail_size, Image.Resampling.LANCZOS)

# Embed the thumbnail into the original image
image.info['thumbnail'] = thumbnail

# Save the image with the embedded thumbnail
output_path = os.path.join(output_dir, 'sample_image_with_thumbnail.jpg')
image.save(output_path, 'JPEG')

print(f"Image saved at {output_path}")