import os
from PIL import Image, ImageDraw
import random

def generate_block_based_compression_image(image_size=(256, 256), block_size=(8, 8), save_path='./tmp/block_compression.jpg'):
    # Create a new image with white background
    img = Image.new('RGB', image_size, color='white')
    draw = ImageDraw.Draw(img)

    # Calculate the number of blocks in both dimensions
    num_blocks_x = image_size[0] // block_size[0]
    num_blocks_y = image_size[1] // block_size[1]

    # Fill each block with a random color
    for x_block in range(num_blocks_x):
        for y_block in range(num_blocks_y):
            # Calculate the top left corner of the current block
            top_left = (x_block*block_size[0], y_block*block_size[1])
            # Calculate the bottom right corner of the current block
            bottom_right = ((x_block+1)*block_size[0], (y_block+1)*block_size[1])
            # Generate a random color
            block_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            # Fill the block with the random color
            draw.rectangle([top_left, bottom_right], fill=block_color)

    # Ensure the save path directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    # Save the image
    img.save(save_path)

# Generate the image
generate_block_based_compression_image()