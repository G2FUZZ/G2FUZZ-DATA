from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image with a specific size
image = Image.new('RGB', (100, 100), 'blue')

# Save the image as BMP
image_path = './tmp/simple_image.bmp'
image.save(image_path)

print(f"Image saved at {image_path}")