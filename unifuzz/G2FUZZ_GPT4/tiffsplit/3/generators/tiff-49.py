import numpy as np
import os
from PIL import Image, ImageDraw

# Create the ./tmp/ directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

def generate_tiff_with_shapes_and_color_depth(filename, color_depth, shape):
    # Generate a base image array
    if color_depth <= 8:
        mode = 'L'  # 8-bit pixels, black and white
        image = Image.new(mode, (100, 100), "white")
    elif color_depth == 24:
        mode = 'RGB'
        image = Image.new(mode, (100, 100), "white")
    elif color_depth == 32:
        mode = 'RGBA'
        image = Image.new(mode, (100, 100), (255, 255, 255, 0))  # Transparent background
    elif color_depth == 48:
        # Simulate 48-bit by using an RGB image with higher resolution
        mode = 'RGB'
        image = Image.new(mode, (100, 100), "white")
    else:
        raise ValueError("Unsupported color depth")
    
    draw = ImageDraw.Draw(image)
    
    if shape == "circle":
        draw.ellipse([25, 25, 75, 75], fill="black")
    elif shape == "square":
        draw.rectangle([25, 25, 75, 75], fill="black")
    else:
        raise ValueError("Unsupported shape")

    # Save the image with a specified color depth
    if color_depth in [8, 24, 32]:
        image.save(filename)
    elif color_depth == 48:
        # For 48-bit, simulate by converting to a higher depth array before saving
        high_depth_array = np.array(image).astype(np.uint16) * 257  # Scale up to simulate 16 bits per channel
        high_depth_image = Image.fromarray(high_depth_array, mode='RGB')
        high_depth_image.save(filename)
    else:
        raise ValueError("Unsupported operation for saving the image with this color depth")

# Generate TIFF files with various color depths and shapes
generate_tiff_with_shapes_and_color_depth('./tmp/shape_color_depth_8bit_circle.tiff', 8, "circle")
generate_tiff_with_shapes_and_color_depth('./tmp/shape_color_depth_24bit_square.tiff', 24, "square")
generate_tiff_with_shapes_and_color_depth('./tmp/shape_color_depth_32bit_circle.tiff', 32, "circle")
generate_tiff_with_shapes_and_color_depth('./tmp/shape_color_depth_48bit_square.tiff', 48, "square")

print("Custom shape TIFF files with various color depths have been generated and saved to ./tmp/")