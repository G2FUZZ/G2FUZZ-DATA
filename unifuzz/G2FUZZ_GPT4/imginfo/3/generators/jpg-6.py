from PIL import Image, ImageDraw

# Create a new image with RGB channels and a white background
width, height = 800, 600
image = Image.new('RGB', (width, height), 'white')

# Draw a simple rectangle as a placeholder for content
draw = ImageDraw.Draw(image)
draw.rectangle([200, 150, 600, 450], outline='black', fill='blue')

# Generate a thumbnail of this image
thumbnail_size = (160, 120)
thumbnail = image.copy()
thumbnail.thumbnail(thumbnail_size)

# Embed the thumbnail within the original image's metadata (EXIF)
# PIL does not directly support inserting thumbnails into the EXIF data,
# so instead, we save the thumbnail as a separate file alongside the main image.
# Please note: The direct embedding of thumbnails into the EXIF metadata of the JPG file
# is not directly supported by PIL/Pillow. As a workaround, this code saves both the image and its thumbnail.

# Ensure the ./tmp/ directory exists
import os
os.makedirs('./tmp/', exist_ok=True)

# Save the original image
image_path = './tmp/image_with_thumbnail.jpg'
image.save(image_path)

# Save the thumbnail with a related name
thumbnail_path = './tmp/image_with_thumbnail_thumbnail.jpg'
thumbnail.save(thumbnail_path)

print(f"Image and its thumbnail have been saved to {image_path} and {thumbnail_path}, respectively.")