from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Create a simple image using PIL
image = Image.new('RGB', (100, 100), (255, 0, 0))
draw = ImageDraw.Draw(image)
draw.ellipse((25, 25, 75, 75), fill=(0, 255, 0))

# Save the image as a progressive JPG
image.save('./tmp/progressive_loading.jpg', 'JPEG', quality=80, progressive=True)