import os
from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the size of the icon
icon_sizes = [(16,16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]

# Creating an image for each size
for size in icon_sizes:
    img = Image.new('RGBA', size, (255, 0, 0, 0)) # Create a new transparent image with red color
    draw = ImageDraw.Draw(img)
    draw.ellipse((0, 0, size[0]-1, size[1]-1), fill=(255, 255, 255, 255), outline=(0, 0, 0, 255))
    
    # Save the image with PNG compression in ICO format
    img.save(f'./tmp/icon_{size[0]}x{size[1]}.ico', format='ICO', sizes=[size])

print("ICO files have been generated and saved in './tmp/'.")