import os
from PIL import Image, ImageDraw

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Create a sample JPEG file with multiple layers and transparency
base = Image.new('RGBA', (200, 200), (255, 255, 255, 255))
layer1 = Image.new('RGBA', (200, 200), (255, 0, 0, 128))
layer2 = Image.new('RGBA', (200, 200), (0, 255, 0, 128))

# Paste layers onto the base image
base.paste(layer1, (0, 0), layer1)
base.paste(layer2, (50, 50), layer2)

# Convert the image to RGB mode before saving as JPEG
base = base.convert('RGB')
base.save('./tmp/sample_complex_features.jpg')

print("JPEG file with multiple layers and transparency created successfully.")