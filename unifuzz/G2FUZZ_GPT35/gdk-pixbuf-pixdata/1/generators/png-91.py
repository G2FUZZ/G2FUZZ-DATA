import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Create a dummy image
image_data = np.random.randint(0, 256, (200, 200, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Add text to the image
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
draw.text((20, 20), "Generated Image with Text", fill=(255, 255, 255), font=font)

# Save the image as a PNG file with text and lossless compression
image.save('./tmp/complex_png_example.png')