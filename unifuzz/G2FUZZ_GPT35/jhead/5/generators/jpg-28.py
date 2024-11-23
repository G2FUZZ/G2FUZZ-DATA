import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Create a white image of size 200x200 pixels
image = np.ones((200, 200, 3), dtype=np.uint8) * 255
image = Image.fromarray(image)

# Add text to the image
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()  # Use a built-in font
draw.text((50, 50), "Hello, World!", fill=(0, 0, 0), font=font)

# Save the image as a jpg file
image.save("./tmp/complex_structure.jpg")

print("Complex structure jpg file generated successfully!")