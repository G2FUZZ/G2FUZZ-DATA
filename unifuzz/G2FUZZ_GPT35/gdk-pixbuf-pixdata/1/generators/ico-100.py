import os
from PIL import Image

# Create a directory for saving generated ICO files
os.makedirs('./tmp/', exist_ok=True)

# Image sizes and color depths for ICO file
images_data = [
    {'size': (16, 16), 'mode': 'RGB'},
    {'size': (32, 32), 'mode': 'RGB'},
    {'size': (48, 48), 'mode': 'RGBA'}
]

# Create images with different sizes and color depths
images = []
for data in images_data:
    new_image = Image.new(data['mode'], data['size'], color='green')
    images.append(new_image)

# Save the images as ICO file with multiple sizes and color depths
ico_file_path = './tmp/icon_multi.ico'
images[0].save(ico_file_path, format='ICO', sizes=[(image.width, image.height) for image in images])