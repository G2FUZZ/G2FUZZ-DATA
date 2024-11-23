import os
from PIL import Image

# Create the ./tmp/ directory if it doesn't exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Generate a basic image
main_image = Image.new('RGB', (800, 600), color = 'blue')

# Generate a thumbnail of this image (to embed)
thumbnail_size = (128, 128)
thumbnail = main_image.copy()
thumbnail.thumbnail(thumbnail_size)

# Save the main image with the thumbnail embedded
main_image.save('./tmp/main_image_with_thumbnail.jpg', 'JPEG', quality=85, thumbnail=thumbnail)