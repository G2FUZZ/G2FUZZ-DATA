from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with RGB channels, 100x100 pixels
image = Image.new('RGB', (100, 100), color = 'blue')

# Save the image with interlacing (passing the 'progressive' argument as True)
image.save('./tmp/interlaced_image.png', 'PNG', progressive=True)