import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Image dimensions
width, height = 800, 600

# Create a new image with 24-bit color (RGB)
image = Image.new("RGB", (width, height))

# Generate a gradient of colors
for x in range(width):
    for y in range(height):
        # Calculate colors
        r = (x % 256)  # Red varies with X
        g = (y % 256)  # Green varies with Y
        b = ((x + y) % 256)  # Blue varies with a combination of X and Y
        image.putpixel((x, y), (r, g, b))

# Save the image
image_path = './tmp/gradient_image.jpg'
image.save(image_path, "JPEG")

print(f"Image saved at {image_path}")