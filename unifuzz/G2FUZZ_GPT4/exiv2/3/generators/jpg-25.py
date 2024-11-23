from PIL import Image, ImageDraw
import os
import random

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Image size
width, height = 256, 256

# Size of each block
block_size = 32

# Function to generate a random color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Function to create a grid image
def create_grid_image():
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)
    for y in range(0, height, block_size):
        for x in range(0, width, block_size):
            draw.rectangle([x, y, x+block_size, y+block_size], fill=random_color(), outline=None)
    return image

# Create and save images
for i in range(3):  # Example: Creating and saving 3 images
    image_path = f'./tmp/block_encoding_example_{i}.jpg'
    img = create_grid_image()
    img.save(image_path)
    print(f"Image {i} saved to {image_path}")