from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with RGB mode
width, height = 200, 200
image = Image.new('RGB', (width, height), 'white')

# Draw a simple rectangle
draw = ImageDraw.Draw(image)
draw.rectangle([50, 50, 150, 150], fill="blue")

# Save the image as a GIF
image.save('./tmp/interlaced_option.gif', 'GIF')

print("GIF saved with an interlacing option.")