from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image using Pillow
img_size = (100, 100)
image = Image.new('RGB', img_size, color = 'blue')
draw = ImageDraw.Draw(image)
draw.text((10, 40), "Hi!", fill='white')

# Define different compression levels (quality)
compression_levels = [25, 50, 75]

for level in compression_levels:
    file_path = f'./tmp/compression_level_{level}.jpg'
    # Save the image with the specified compression level (quality)
    image.save(file_path, 'JPEG', quality=level)

print("Images have been saved with different compression levels.")