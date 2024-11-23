import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Create a white image with black text
text = "Wide browser support: PNG files are widely supported by web browsers and image editing software."
image = Image.new('RGB', (800, 100), color='white')
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
draw.text((10, 10), text, fill='black', font=font)

# Save the image
image.save('./tmp/wide_browser_support.png')