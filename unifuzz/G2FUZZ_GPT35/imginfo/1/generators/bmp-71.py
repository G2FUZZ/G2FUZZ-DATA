import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Create a new RGBA image with transparency
width, height = 200, 200
transparent_color = (0, 0, 0, 0)  # Transparent black
image = Image.new('RGBA', (width, height), transparent_color)

# Draw text on the image
draw = ImageDraw.Draw(image)
text = "Hello, BMP!"
font = ImageFont.load_default()  # Load default font
text_width, text_height = draw.textsize(text, font)
text_position = ((width - text_width) // 2, (height - text_height) // 2)
draw.text(text_position, text, fill=(255, 255, 255, 255), font=font)

# Save the image as a BMP file with a custom file name
file_name = './tmp/custom_bmp_image.bmp'
image.save(file_name)