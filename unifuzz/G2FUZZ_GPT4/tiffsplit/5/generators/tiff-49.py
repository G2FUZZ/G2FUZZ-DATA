from PIL import Image, ImageDraw
import numpy as np
import os

def create_gradient(width, height):
    """Generate a gradient image."""
    image_data = np.zeros((height, width, 3), dtype=np.uint16)
    for y in range(height):
        for x in range(width):
            image_data[y, x, 0] = (x * 65535) // width  # Red channel gradient
            image_data[y, x, 1] = (y * 65535) // height  # Green channel gradient
            image_data[y, x, 2] = ((x + y) * 65535) // (width + height)  # Blue channel mix
    return Image.fromarray(image_data, mode='I;16')

def create_circle_pattern(width, height):
    """Generate an image with circles."""
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)
    spacing = width // 10
    radius = spacing // 2
    for y in range(0, height, spacing):
        for x in range(0, width, spacing):
            left_up_point = (x - radius, y - radius)
            right_down_point = (x + radius, y + radius)
            draw.ellipse([left_up_point, right_down_point], fill=(int(255 * (x / width)), int(255 * (y / height)), 127))
    return image.convert('I;16')

def create_checkerboard(width, height):
    """Generate a checkerboard pattern."""
    image_data = np.zeros((height, width), dtype=np.uint16)
    check_size = width // 10
    for y in range(height):
        for x in range(width):
            if (x // check_size) % 2 == (y // check_size) % 2:
                image_data[y, x] = 65535  # White
            else:
                image_data[y, x] = 0  # Black
    return Image.fromarray(image_data, mode='I;16')

def save_tiff_with_layers(file_path, images, compression='tiff_lzw'):
    """Save multiple images as layers (pages) in a single TIFF file."""
    images[0].save(
        file_path,
        save_all=True,
        append_images=images[1:],
        compression=compression,
        format='TIFF'
    )

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define image size
width, height = 256, 256

# Create images for layers
gradient_image = create_gradient(width, height)
circle_image = create_circle_pattern(width, height)
checkerboard_image = create_checkerboard(width, height)

# Save the images as layers in a single TIFF file
file_path = './tmp/complex_high_color_depth.tiff'
save_tiff_with_layers(file_path, [gradient_image, circle_image, checkerboard_image])

print(f"Complex TIFF image with multiple layers saved to {file_path}")