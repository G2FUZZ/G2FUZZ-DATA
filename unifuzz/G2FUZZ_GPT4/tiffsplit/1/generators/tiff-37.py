from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a gradient image
def generate_gradient_image(width, height, mode):
    if mode == 'L':  # Grayscale
        image = np.zeros((height, width), dtype=np.uint8)
        channels = 1
    elif mode in ['RGB', 'RGBA']:
        image = np.zeros((height, width, len(mode)), dtype=np.uint8)
        channels = len(mode)
    else:
        raise ValueError("Unsupported mode")

    # Creating a gradient effect for our image
    for i in range(height):
        for j in range(width):
            if channels == 1:  # Grayscale
                image[i, j] = (i + j) % 256
            else:  # RGB or RGBA
                for k in range(channels):
                    image[i, j, k] = (i + j + k*42) % 256  # Arbitrary operation for demonstration

    return Image.fromarray(image, mode)

# Generate images with different sizes and color modes
width, height = 256, 256
images = [
    generate_gradient_image(width, height, 'L'),  # Grayscale image
    generate_gradient_image(width, height, 'RGB'),  # RGB image
    generate_gradient_image(width, height, 'RGBA'),  # RGBA image
]

# Save the images as a multi-page TIFF
# NOTE: The 'save_all' and 'append_images' options are used for multi-page TIFFs
images[0].save('./tmp/complex_structure.tiff', save_all=True, append_images=images[1:], compression='tiff_lzw')

print("Multi-page TIFF with complex structures has been saved.")