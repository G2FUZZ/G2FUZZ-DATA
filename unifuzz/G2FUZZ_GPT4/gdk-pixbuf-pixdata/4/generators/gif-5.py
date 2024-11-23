from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Create a new image with RGB mode
image = Image.new('RGB', (200, 200), color = (73, 109, 137))

# Draw some shapes on the image
draw = ImageDraw.Draw(image)
draw.ellipse((50, 50, 150, 150), fill=(255, 87, 34), outline=(255, 255, 255))
draw.rectangle((50, 50, 150, 150), outline=(0, 255, 0))

# Save the image with interlacing enabled
image.save('./tmp/interlaced_image.gif', 'GIF', interlace=1)