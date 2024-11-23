import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Define the dimensions of the image
width = 600
height = 400

# Create a blank RGB image
image = np.zeros((height, width, 3), dtype=np.uint8)

# Fill the background with a gradient color
for i in range(width):
    for j in range(height):
        image[j, i] = [i % 256, j % 256, (i + j) % 256]

# Create a PIL image from the numpy array
image_pil = Image.fromarray(image, 'RGB')

# Add shapes to the image
draw = ImageDraw.Draw(image_pil)

# Draw a rectangle
draw.rectangle([(50, 50), (200, 150)], fill=(255, 0, 0))

# Draw a circle
draw.ellipse([(300, 100), (450, 250)], fill=(0, 255, 0))

# Add text to the image using a system font (Times New Roman)
font = ImageFont.load_default()
text = "Complex Image with Shapes"
text_width, text_height = draw.textsize(text, font)
text_position = ((width - text_width) // 2, (height - text_height) // 2)
draw.text(text_position, text, fill=(255, 255, 255), font=font)

# Save the image to a file in JPEG format
image_pil.save('./tmp/complex_image_extended.jpg', 'JPEG')

print("Complex Image with Shapes saved successfully.")