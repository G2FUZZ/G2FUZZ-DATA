from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists or create it
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Create a simple image with PIL
image = Image.new('RGB', (100, 100), 'blue')
draw = ImageDraw.Draw(image)
draw.text((10, 10), "Hi!", fill='white')

# Save the image as a progressive JPEG
image.save('./tmp/progressive_image.jpg', 'JPEG', quality=80, progressive=True)