import numpy as np
from PIL import Image, ImageDraw, ImageFilter

# Create an array with random pixel values
width, height = 100, 100
pixels = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

# Create PIL image from the pixel array
image = Image.fromarray(pixels)

# Add text to the image
draw = ImageDraw.Draw(image)
text = "Hello, World!"
draw.text((10, 10), text, fill=(255, 255, 255))  # White text at position (10, 10)

# Apply a filter to the image
image = image.filter(ImageFilter.GaussianBlur(radius=2))

# Save the image with more complex file structures
image.save('./tmp/complex_generated_image.jpg', quality=90, optimize=True)

# Confirming the editing limitations message
print("Editing limitations: JPG files are lossy, so repeated edits and saves can degrade image quality.")