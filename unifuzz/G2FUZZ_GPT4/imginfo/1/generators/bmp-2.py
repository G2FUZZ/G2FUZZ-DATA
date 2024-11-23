import os
from PIL import Image
import numpy as np

# Create the target directory if it doesn't exist
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Define the image size and the color depth values to be used
image_size = (100, 100)  # Width, height in pixels
color_depths = [1, 4, 8, 24, 32]  # Adjusted color depths to those feasible for BMP

def generate_color_gradient(size, color_depth):
    """
    Generates a simple color gradient based on the color depth.
    For 1-bit, it's just a black and white image.
    For higher color depths, a more complex gradient is used.
    """
    if color_depth == 1:
        # For 1-bit, create a checkerboard pattern
        img = np.zeros(size, dtype=np.uint8)
        img[::2, ::2] = 255  # Every other pixel black/white
        img[1::2, 1::2] = 255
        img = Image.fromarray(img, mode='1')
    else:
        # For higher color depths, create a gradient
        x = np.linspace(0, 255, size[0])
        y = np.linspace(0, 255, size[1])
        xv, yv = np.meshgrid(x, y)
        if color_depth in [4, 8]:
            img = (xv + yv) % 256  # Simple pattern for 8-bit
            img = Image.fromarray(img.astype(np.uint8), mode='L')
        elif color_depth == 24:
            # For 24-bit, create an RGB image
            img = np.stack([(xv % 256).astype(np.uint8), (yv % 256).astype(np.uint8), 
                            ((xv + yv) % 256).astype(np.uint8)], axis=-1)
            img = Image.fromarray(img, mode='RGB')
        elif color_depth == 32:
            # For 32-bit, create an RGBA image
            img = np.stack([(xv % 256).astype(np.uint8), (yv % 256).astype(np.uint8), 
                            ((xv + yv) % 256).astype(np.uint8), np.full_like(xv, 255)], axis=-1)
            img = Image.fromarray(img, mode='RGBA')
    return img

for depth in color_depths:
    # Generate the image based on the color depth
    img = generate_color_gradient(image_size, depth)
    # Save the image
    img.save(os.path.join(output_dir, f"gradient_{depth}bit.bmp"))

print("Images generated successfully.")