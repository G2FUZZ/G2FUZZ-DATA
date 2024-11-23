import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

# Create a sample image
image_data = np.random.randint(0, 256, size=(200, 200, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Add text overlay to the image
draw = ImageDraw.Draw(image)
text = "Complex PNG Image"
font = ImageFont.load_default()
draw.text((50, 50), text, fill=(255, 255, 255), font=font)

# Draw shapes on the image
draw.rectangle([100, 100, 150, 150], outline=(255, 0, 0), width=2)
draw.ellipse([50, 100, 100, 150], outline=(0, 255, 0), width=2)

# Save the image with additional complexity
image.save('./tmp/complex_image.png')