import os
from PIL import Image

# Create a directory for saving generated ICO files
os.makedirs('./tmp/', exist_ok=True)

# Image sizes and resolutions for ICO file
sizes = [(16, 16), (32, 32), (48, 48)]

# Create images with different resolutions
images = []
for size in sizes:
    new_image = Image.new('RGBA', size, color='red')
    images.append(new_image)

# Save the images as ICO file
images[0].save('./tmp/icon.ico', format='ICO', sizes=[(image.width, image.height) for image in images])