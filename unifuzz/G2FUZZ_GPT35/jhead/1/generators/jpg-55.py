import numpy as np
from PIL import Image, ImageDraw, ImageFilter

# Define the dimensions of the image
width = 800
height = 600

# Create a blank RGBA image (with alpha channel for transparency)
image = np.zeros((height, width, 4), dtype=np.uint8)

# Create a background gradient
for y in range(height):
    for x in range(width):
        image[y, x] = [x, y, 150, 255]  # RGBA values based on position for gradient effect

# Convert the numpy array to a PIL Image with 'RGBA' mode
image = Image.fromarray(image, 'RGBA')

# Create a new layer for shapes
shape_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
draw = ImageDraw.Draw(shape_layer)

# Draw shapes on the shape layer
draw.rectangle([100, 100, 300, 300], fill=(255, 0, 0, 150))  # Semi-transparent red rectangle
draw.ellipse([400, 100, 600, 300], fill=(0, 255, 0, 150))  # Semi-transparent green ellipse

# Combine the background and shape layers
image = Image.alpha_composite(image.convert('RGBA'), shape_layer)

# Add text to the image
draw = ImageDraw.Draw(image)
text = "Complex Image with Shapes and Gradient"
draw.text((50, 50), text, fill=(255, 255, 255))

# Apply a filter effect
image = image.filter(ImageFilter.GaussianBlur(radius=2))

# Convert the image to RGB mode before saving as JPEG
image = image.convert('RGB')

# Save the image to a file
image.save('./tmp/complex_image_extended.jpg')

print("Extended Complex Image saved successfully.")