from PIL import Image, ImageDraw

# Create a new image with RGB channels
width, height = 800, 600
image = Image.new('RGB', (width, height))

# Create a gradient
draw = ImageDraw.Draw(image)
for i in range(width):
    for j in range(height):
        # Gradient from black to red, green, and blue
        red = int((i/width) * 255)
        green = int((j/height) * 255)
        blue = 255 - red
        draw.point((i, j), fill=(red, green, blue))

# Ensure the ./tmp/ directory exists
import os
os.makedirs('./tmp/', exist_ok=True)

# Save the image with chroma subsampling (4:2:0)
image.save('./tmp/chroma_subsampling_example.jpg', 'JPEG', quality=85, subsampling='4:2:0')