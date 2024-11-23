import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Create a white image of size 400x400 pixels
image = np.ones((400, 400, 3), dtype=np.uint8) * 255
image = Image.fromarray(image)

# Add shapes and text to the image
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()  # Use a built-in font

# Draw a red circle
draw.ellipse((50, 50, 150, 150), fill=(255, 0, 0))

# Draw a blue rectangle
draw.rectangle((100, 100, 200, 200), fill=(0, 0, 255))

# Add text
draw.text((50, 200), "Complex Structure", fill=(0, 0, 0), font=font)

# Save the image as a jpg file
image.save("./tmp/complex_structure_extended.jpg")

print("Complex structure with multiple shapes and text jpg file generated successfully!")