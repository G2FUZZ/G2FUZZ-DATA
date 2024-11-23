import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Create a white image
img = Image.fromarray(np.ones((100, 100, 3), dtype=np.uint8) * 255)

# Add text to the image
draw = ImageDraw.Draw(img)
font = ImageFont.load_default()  # Using default font
draw.text((10, 10), "Hello, JPG File!", fill=(0, 0, 0), font=font)

# Save the image with text as a jpg file
img.save("./tmp/complex_jpg_file.jpg")