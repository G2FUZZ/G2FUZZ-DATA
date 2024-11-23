from PIL import Image, ImageDraw

# Create a new image with white background
width, height = 800, 600
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Draw some patterns
for i in range(0, width, 100):
    for j in range(0, height, 100):
        if (i+j) // 100 % 2 == 0:
            draw.rectangle([i, j, i+100, j+100], fill='lightblue')

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image with PNG format which uses lossless compression
image.save('./tmp/lossless_compression_demo.png')