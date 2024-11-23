import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an image with transparency
width, height = 200, 200
transparent_image = Image.new('RGBA', (width, height), (255, 255, 255, 0))

# Let's draw a simple red circle in the middle with some transparency
from PIL import ImageDraw

draw = ImageDraw.Draw(transparent_image)
# Drawing a circle with red color and half-transparent
draw.ellipse((50, 50, 150, 150), fill=(255, 0, 0, 128))

# Save the image
transparent_image.save('./tmp/transparent_image.png')