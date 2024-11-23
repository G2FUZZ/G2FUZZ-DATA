from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with a white background
image = Image.new('RGB', (200, 200), 'white')
draw = ImageDraw.Draw(image)

# Draw a simple red rectangle
draw.rectangle([50, 50, 150, 150], fill="red")

# Save the image with JPEG compression to ./tmp/
image_path = './tmp/test_image.jpg'
image.save(image_path, 'JPEG')

print(f"Image saved to {image_path}")