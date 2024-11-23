from PIL import Image, ImageSequence
import numpy as np
import os

def create_gradient_image(width, height, start_color, end_color):
    """
    Generate a simple gradient image from start_color to end_color.
    """
    image_data = np.zeros((height, width, 3), dtype=np.uint8)
    for x in range(width):
        for y in range(height):
            image_data[y, x] = [
                start_color[0] + (end_color[0] - start_color[0]) * x // width,
                start_color[1] + (end_color[1] - start_color[1]) * y // height,
                start_color[2] + (end_color[2] - start_color[2]) * (x + y) // (width + height)
            ]
    return Image.fromarray(image_data, 'RGB')

def add_metadata(image, metadata):
    """
    Add metadata to an image. Metadata should be a dictionary where keys are the tag names.
    Note: This function just demonstrates how one might add metadata, but PIL's support for reading/writing
    metadata (especially in TIFFs) is limited and might not work for all tags without additional libraries.
    """
    for key, value in metadata.items():
        image.info[key] = value
    return image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a multi-page TIFF image
width, height = 256, 256
images = []

# Generate different gradient images to simulate multiple pages
colors = [((0, 0, 255), (255, 0, 0)), ((0, 255, 0), (0, 0, 255)), ((255, 0, 0), (0, 255, 0))]
for start_color, end_color in colors:
    img = create_gradient_image(width, height, start_color, end_color)
    img = add_metadata(img, {'Description': f'Gradient from {start_color} to {end_color}'})
    images.append(img)

# Save the images as a multi-page TIFF
images[0].save(
    './tmp/multi_page_tiff_with_metadata.tiff',
    save_all=True,
    append_images=images[1:],
    compression='tiff_lzw',
    dpi=(300,300),  # Example of setting the DPI for each image/page
    metadata={'Software': 'PIL'}
)

print("Multi-page TIFF with metadata has been saved.")