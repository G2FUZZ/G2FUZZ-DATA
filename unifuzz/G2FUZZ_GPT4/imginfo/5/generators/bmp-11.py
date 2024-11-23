from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with width=100, height=100
width, height = 100, 100
image = Image.new('RGB', (width, height), 'blue')

# Save the image as BMP
file_path = './tmp/simple_image.bmp'
image.save(file_path)

print(f"Image saved to {file_path}")