from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a base image
img = Image.new('RGB', (800, 600), color='blue')

# Optionally, draw some content on the image
draw = ImageDraw.Draw(img)
draw.text((10, 10), "Sample Image", fill="white")

# Create a thumbnail of the base image
thumbnail_size = (128, 128)
thumbnail = img.copy()
thumbnail.thumbnail(thumbnail_size)

# Save the thumbnail within the original image info
img.info['thumbnail'] = thumbnail

# Save the image with an embedded thumbnail to a file
output_path = os.path.join(output_dir, 'sample_with_thumbnail.jpg')
img.save(output_path, 'JPEG')

print(f"Image with embedded thumbnail saved to {output_path}")