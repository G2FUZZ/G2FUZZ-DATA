from PIL import Image, ImageDraw

# Create a new image with white background
img = Image.new('RGB', (200, 200), color = 'white')

# Draw a simple red rectangle
d = ImageDraw.Draw(img)
d.rectangle([50, 50, 150, 150], fill ="red")

# Ensure the './tmp/' directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image as progressive JPEG
img.save('./tmp/progressive_example.jpg', 'JPEG', quality=80, progressive=True)