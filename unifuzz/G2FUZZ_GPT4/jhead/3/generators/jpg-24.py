import os
from PIL import Image, ImageDraw
import random
import numpy as np

def generate_complex_image(image_size=(256, 256), save_path='./tmp/complex_block_compression.jpg', max_block_size=32):
    # Create a new image with white background
    img = Image.new('RGB', image_size, color='white')
    draw = ImageDraw.Draw(img)

    # Initialize the top left corner of the first block
    x_start, y_start = 0, 0

    while x_start < image_size[0]:
        y_start = 0
        # Randomly determine the current block's width, not exceeding the image's width
        block_width = random.randint(8, max_block_size)
        while y_start < image_size[1]:
            # Randomly determine the current block's height, not exceeding the image's height
            block_height = random.randint(8, max_block_size)
            # Calculate the bottom right corner of the current block
            bottom_right = (x_start + block_width, y_start + block_height)

            # Generate a gradient within the block
            top_left_color = np.array([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
            bottom_right_color = np.array([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
            for x in range(x_start, min(x_start + block_width, image_size[0])):
                for y in range(y_start, min(y_start + block_height, image_size[1])):
                    # Interpolate the color for the current pixel
                    alpha = (x - x_start) / block_width
                    beta = (y - y_start) / block_height
                    pixel_color = (1 - alpha) * (1 - beta) * top_left_color + alpha * beta * bottom_right_color
                    # Simulate compression by reducing color depth
                    pixel_color = (pixel_color // 32 * 32).astype(int)
                    img.putpixel((x, y), tuple(pixel_color))

            y_start += block_height

        x_start += block_width

    # Ensure the save path directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    # Save the image
    img.save(save_path)

# Generate the complex image
generate_complex_image()