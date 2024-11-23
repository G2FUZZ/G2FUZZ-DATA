from PIL import Image
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Create a sample image
image = Image.new('RGB', (800, 600), color = 'blue')

# Create a thumbnail
thumbnail_size = (128, 128)
thumbnail = image.copy()
thumbnail.thumbnail(thumbnail_size)

# Save the image
output_path = os.path.join(output_dir, 'image.jpg')
image.save(output_path, 'JPEG', quality=85)

# Save the thumbnail
thumbnail_path = os.path.join(output_dir, 'thumbnail.jpg')
thumbnail.save(thumbnail_path, 'JPEG', quality=85)

print(f"Image saved to {output_path}")
print(f"Thumbnail saved to {thumbnail_path}")