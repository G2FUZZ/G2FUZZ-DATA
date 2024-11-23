from PIL import Image, ImageDraw

# Create an image with transparent background
width, height = 400, 400
image = Image.new('RGBA', (width, height), (255, 0, 0, 0))

# Draw a red circle in the center with some transparency
draw = ImageDraw.Draw(image)
radius = 100
left_up_point = (width / 2 - radius, height / 2 - radius)
right_down_point = (width / 2 + radius, height / 2 + radius)
draw.ellipse([left_up_point, right_down_point], fill=(255, 0, 0, 128))

# Make sure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image
image.save('./tmp/transparent_example.png')