import numpy as np
from PIL import Image

# Create a new image with white background
width, height = 200, 100
image = Image.new('RGB', (width, height), color='white')

# Add text to the image
from PIL import ImageDraw, ImageFont
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
text = "PNG files can embed textual data like comments or descriptions."
draw.text((10, 10), text, fill='black', font=font)

# Save the image
image.save("./tmp/textual_data.png")