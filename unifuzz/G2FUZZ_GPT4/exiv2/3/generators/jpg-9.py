from PIL import Image, ImageDraw
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Image size
width, height = 256, 256  # To make a grid of 8x8 blocks in a 256x256 image

# Create a new image with white background
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Size of each block
block_size = 32  # For 8x8 blocks in a 256x256 image

# Function to generate a random color
import random
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Draw the blocks
for y in range(0, height, block_size):
    for x in range(0, width, block_size):
        draw.rectangle([x, y, x+block_size, y+block_size], fill=random_color(), outline=None)

# Save the image
image_path = './tmp/block_encoding_example.jpg'
image.save(image_path, 'JPEG')

print(f"Image saved to {image_path}")