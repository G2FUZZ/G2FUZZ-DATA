import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import random

def generate_complex_image(image_size=(256, 256), block_size=(8, 8), text="Sample Text", save_path='./tmp/complex_block_compression.jpg'):
    # Create a new image with white background
    img = Image.new('RGB', image_size, color='white')
    draw = ImageDraw.Draw(img)

    # Calculate the number of blocks in both dimensions
    num_blocks_x = image_size[0] // block_size[0]
    num_blocks_y = image_size[1] // block_size[1]

    for x_block in range(num_blocks_x):
        for y_block in range(num_blocks_y):
            top_left = (x_block*block_size[0], y_block*block_size[1])
            bottom_right = ((x_block+1)*block_size[0], (y_block+1)*block_size[1])
            
            # Instead of a single random color, generate a gradient within the block
            start_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            end_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            for i, color in enumerate(interpolate_colors(start_color, end_color, block_size[0])):
                draw.line([(top_left[0] + i, top_left[1]), (top_left[0] + i, bottom_right[1])], fill=color, width=1)

    # Add a text overlay to the image
    try:
        font = ImageFont.truetype("arial.ttf", size=20)  # Adjust the path to the font file as necessary
    except IOError:
        font = ImageFont.load_default()
    
    # Workaround for text size estimation
    # This is a rough estimation and not accurate
    text_width = len(text) * font.size  # This is a simplistic approximation
    text_height = font.size  # Also a simplistic approximation
    text_position = ((image_size[0] - text_width) // 2, (image_size[1] - text_height) // 2)
    draw.text(text_position, text, fill=(255, 255, 255), font=font)

    # Apply a simple blur filter to the entire image
    img = img.filter(ImageFilter.BLUR)

    # Ensure the save path directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    # Save the image
    img.save(save_path)

def interpolate_colors(color_start, color_end, steps):
    """Generate a list of colors forming a gradient between two specified colors."""
    step_factor = [(color_end[i] - color_start[i]) / steps for i in range(3)]
    return [(int(color_start[0] + step_factor[0] * step), 
             int(color_start[1] + step_factor[1] * step), 
             int(color_start[2] + step_factor[2] * step)) for step in range(steps)]

# Generate the complex image
generate_complex_image()