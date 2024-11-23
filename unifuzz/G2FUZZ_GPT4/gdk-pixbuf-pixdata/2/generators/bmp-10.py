import os
from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Create a new image with a white background
width, height = 200, 200
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Draw a simple red rectangle to illustrate the single layer
rectangle_start = (50, 50)
rectangle_end = (150, 150)
draw.rectangle([rectangle_start, rectangle_end], fill='red')

# Save the image as a BMP file
output_path = os.path.join(output_dir, 'no_layers_example.bmp')
image.save(output_path, format='BMP')

print(f'BMP image saved to {output_path}')