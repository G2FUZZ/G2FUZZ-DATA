from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image
image = Image.new('RGB', (100, 100), color = 'blue')

# Save the image without explicitly embedding an ICC profile
image.save('./tmp/simple_image.jpg', 'JPEG')

print("Image was saved without embedding an ICC profile.")