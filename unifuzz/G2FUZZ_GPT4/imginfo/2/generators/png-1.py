import os
from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with white background
width, height = 400, 200
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Draw a rectangle and some text
draw.rectangle([70, 50, 330, 150], outline="red", width=3)
draw.text((100, 100), "Lossless Compression", fill="black")

# Save the image as PNG
file_path = './tmp/lossless_compression_demo.png'
image.save(file_path, "PNG")

print(f"Image saved to {file_path}")