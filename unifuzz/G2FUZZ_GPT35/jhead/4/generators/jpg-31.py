import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Create a 100x100 random image
image = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
image = Image.fromarray(image)

# Add text to the image
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()  # Load default font
draw.text((10, 10), "Generated Image", fill=(255, 255, 255), font=font)

# Save the image as a JPG file with text added
image.save('./tmp/complex_image.jpg')