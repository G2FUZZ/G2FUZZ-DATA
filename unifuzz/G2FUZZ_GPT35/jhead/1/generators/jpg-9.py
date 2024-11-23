import numpy as np
from PIL import Image

# Create a white image with specified dimensions
width = 100
height = 100
image = Image.new('RGB', (width, height), color='white')

# Add text indicating layer support
from PIL import ImageDraw, ImageFont
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
text = "Layer support: JPG files do not support layers like formats such as PSD (Photoshop) or TIFF."
draw.text((10, 10), text, fill='black', font=font)

# Save the image as a jpg file
image.save('./tmp/layer_support.jpg')

print("Image saved successfully!")