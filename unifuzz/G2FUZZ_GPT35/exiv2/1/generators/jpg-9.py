import numpy as np
from PIL import Image

# Create a blank white image
width, height = 800, 600
img = Image.new('RGB', (width, height), color='white')

# Add text indicating the number of layers
from PIL import ImageDraw, ImageFont
draw = ImageDraw.Draw(img)
font = ImageFont.load_default()  # Use a system default font
text = "Layers: JPG files do not support multiple layers like PSD files."
text_width, text_height = draw.textsize(text, font)
text_position = ((width - text_width) // 2, (height - text_height) // 2)
draw.text(text_position, text, fill='black', font=font)

# Save the image
img.save('./tmp/layers.jpg')