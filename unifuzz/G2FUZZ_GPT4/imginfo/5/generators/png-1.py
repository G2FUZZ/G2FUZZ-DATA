from PIL import Image, ImageDraw

# Ensure the tmp directory exists
import os
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Create a new image with white background
width, height = 300, 300
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Draw a simple repeating pattern that demonstrates lossless compression well
for x in range(0, width, 10):
    for y in range(0, height, 10):
        if (x // 10) % 2 == (y // 10) % 2:
            draw.rectangle([x, y, x+9, y+9], fill='black')

# Save the image as PNG
image.save('./tmp/lossless_compression_demo.png')

print('PNG file with a demonstration of lossless compression has been saved to ./tmp/')