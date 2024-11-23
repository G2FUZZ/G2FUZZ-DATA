import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Create a white image
image_data = np.ones((200, 200, 3), dtype=np.uint8) * 255
image = Image.fromarray(image_data)

# Draw text on the image
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()  # Use a built-in font
draw.text((50, 50), "Hello, World!", fill=(0, 0, 0), font=font)

# Save the image as jpg file
image.save("./tmp/complex_structure.jpg")