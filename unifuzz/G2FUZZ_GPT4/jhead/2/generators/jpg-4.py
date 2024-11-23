from PIL import Image, ImageDraw
import os

# Ensure ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a base image
base_image = Image.new('RGB', (800, 600), (255, 200, 100))

# Optionally, draw some content on the image
draw = ImageDraw.Draw(base_image)
draw.text((10, 10), "Sample Image", fill=(0, 0, 0))

# Create a thumbnail
thumbnail_size = (128, 96)
thumbnail = base_image.copy()
thumbnail.thumbnail(thumbnail_size)

# Save the thumbnail within the image's info dictionary
# Note: This doesn't embed the thumbnail as part of the image content but stores it in a way
# that some software can use to quickly display a preview.
base_image.info['thumbnail'] = thumbnail

# Save the image along with its thumbnail
file_path = os.path.join(output_dir, 'image_with_thumbnail.jpg')
base_image.save(file_path, "JPEG")

print(f"Image with embedded thumbnail saved to {file_path}")