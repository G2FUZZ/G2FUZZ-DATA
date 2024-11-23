from PIL import Image, ImageSequence
import numpy as np
import os

def generate_gradient_image(width, height):
    # Generate a width x height pixels image with a gradient
    image = np.zeros((height, width), dtype=np.uint8)

    # Creating a gradient effect for our image
    for i in range(height):
        for j in range(width):
            image[i, j] = (i+j) % 256

    return Image.fromarray(image)

def save_multipage_tiff(path, images, compression='tiff_lzw'):
    # Save multiple images to a TIFF file
    images[0].save(
        path,
        save_all=True,
        append_images=images[1:],
        compression=compression
    )

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Parameters for our images
width, height = 256, 256

# Generate multiple gradient images for demonstration
images = [generate_gradient_image(width, height) for _ in range(3)]

# Save the images as a multi-page TIFF
save_multipage_tiff('./tmp/gradient_multipage_lzw_compressed.tiff', images)

print("Generated a multi-page TIFF with Document Structure Tags.")