import os
from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Create a transparent PNG image
width, height = 200, 200
image = Image.new('RGBA', (width, height), (255, 0, 0, 0)) # Transparent background

# Draw a simple shape with transparency
draw = ImageDraw.Draw(image)
draw.rectangle([50, 50, 150, 150], fill=(255, 0, 0, 128))  # Semi-transparent red square

# Save the image
file_path = os.path.join(output_dir, 'transparent_image.png')
image.save(file_path)

print(f"Image saved to {file_path}")