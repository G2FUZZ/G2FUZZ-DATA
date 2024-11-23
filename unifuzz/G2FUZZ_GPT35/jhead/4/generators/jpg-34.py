import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Create a 100x100 random image
image = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
image = Image.fromarray(image)

# Add text to the image
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()  # Load default font
draw.text((10, 10), "Generated Image", fill=(255, 255, 255), font=font)

# Add shapes to the image
draw.rectangle([20, 20, 80, 80], outline=(255, 0, 0))  # Red rectangle
draw.ellipse([30, 30, 70, 70], outline=(0, 255, 0))  # Green circle

# Save the image as a JPG file with text and shapes added
image.save('./tmp/complex_image_with_shapes.jpg')