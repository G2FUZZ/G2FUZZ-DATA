import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image
image = Image.new('RGB', (100, 100), color='red')

# Path to save the image
output_path = './tmp/image.jpg'

# Save the image without explicitly embedding an ICC profile
image.save(output_path)

print(f"Image saved at: {output_path}")