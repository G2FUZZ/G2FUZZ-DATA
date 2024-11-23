import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Create a blank image
image = Image.new('RGB', (400, 400), color=(255, 255, 255))

# Add rectangle shape to the image
draw = ImageDraw.Draw(image)
draw.rectangle([(50, 50), (150, 150)], fill=(255, 0, 0), outline=(0, 0, 0))

# Add circle shape to the image
draw.ellipse((200, 200, 300, 300), fill=(0, 255, 0), outline=(0, 0, 0))

# Add text to the image using a default font
font = ImageFont.load_default()
draw.text((20, 20), "Advanced PNG with Shapes and Text", fill=(0, 0, 0), font=font)

# Apply a blur filter to the image
blurred_image = image.filter(ImageFilter.GaussianBlur(radius=2))

# Save the image as a PNG file with shapes, text, and blur effect
blurred_image.save('./tmp/advanced_png_example.png')