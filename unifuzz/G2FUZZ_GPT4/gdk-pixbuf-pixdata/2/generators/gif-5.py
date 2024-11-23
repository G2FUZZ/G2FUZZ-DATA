from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Create a new image with white background
width, height = 200, 200
image = Image.new('RGB', (width, height), 'white')

# Optionally, draw something on the image
draw = ImageDraw.Draw(image)
draw.ellipse((50, 50, 150, 150), fill='blue', outline='black')

# Enable interlace
image.info['interlace'] = True

# Save the image as GIF with interlacing
image.save('./tmp/interlaced_image.gif', 'GIF', interlace=0)