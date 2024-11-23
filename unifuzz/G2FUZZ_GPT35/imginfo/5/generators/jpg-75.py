import numpy as np
from PIL import Image, ImageDraw, ImageFilter

# Create a new image with a black background
image = Image.new('RGB', (200, 200), color='black')

# Add text to the image
draw = ImageDraw.Draw(image)
text = "Hello, World!"
draw.text((50, 50), text, fill='white')

# Apply a filter effect to the image
image = image.filter(ImageFilter.BLUR)

# Save the image with .jpg extension
image.save("./tmp/complex_image.jpg")