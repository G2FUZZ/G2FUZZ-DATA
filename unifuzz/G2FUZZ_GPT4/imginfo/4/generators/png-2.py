from PIL import Image
import os

# Create an image with RGBA (Red, Green, Blue, Alpha) mode with transparency
width, height = 400, 400
image = Image.new('RGBA', (width, height))

# Create a gradient of transparency
for x in range(width):
    for y in range(height):
        # Gradient calculation: The further to the right, the less transparent (higher alpha value)
        alpha = int(255 * (x / width))
        image.putpixel((x, y), (255, 105, 180, alpha))  # Pink color with calculated alpha

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Save the image
image.save('./tmp/transparent_gradient.png')