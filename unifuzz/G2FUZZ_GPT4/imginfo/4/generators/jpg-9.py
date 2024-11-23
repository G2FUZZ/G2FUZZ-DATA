from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with white background
image = Image.new('RGB', (100, 100), 'white')
draw = ImageDraw.Draw(image)

# Draw a simple element; let's say a red rectangle
draw.rectangle([10, 10, 90, 90], outline='red', fill='red')

# Save the image with Huffman coding compression
image_path = './tmp/simple_image.jpg'
image.save(image_path, 'JPEG')

print(f"Image saved at {image_path}")