import os
from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a new image with white background
image = Image.new('RGB', (200, 200), 'white')
draw = ImageDraw.Draw(image)

# Draw a red rectangle
draw.rectangle([50, 50, 150, 150], outline='red', fill='red')

# Draw a blue circle. PIL expects a bounding box for the circle.
draw.ellipse([75, 75, 125, 125], outline='blue', fill='blue')

# Draw a green line
draw.line((50, 100, 150, 100), fill='green', width=2)

# Save the image as BMP
bmp_path = os.path.join(output_dir, 'device_independence.bmp')
image.save(bmp_path, 'BMP')

print(f"BMP file saved at {bmp_path}")