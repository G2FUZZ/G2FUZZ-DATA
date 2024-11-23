import numpy as np
from PIL import Image

# Create a new PNG image
image = Image.new('RGB', (100, 100), color='white')

# Add text to the image
from PIL import ImageDraw, ImageFont

draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

text = "PNG file with text support"
draw.text((10, 40), text, fill='black', font=font)

# Save the image
image.save("./tmp/text_support.png")