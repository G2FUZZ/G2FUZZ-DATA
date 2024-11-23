from PIL import Image, ImageDraw
import numpy as np
import os

def create_image_data(width, height):
    """Create a numpy array with random data for image creation."""
    # Generate an image with custom patterns
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=(int(0.5*x) % 256, int(0.5*y) % 256, (x+y) % 256))
    return np.array(image)

def save_multipage_tiff(output_path, images_data, compression_method, custom_tags):
    """
    Save multiple images as a multi-page TIFF with custom tags.

    Parameters:
    - output_path: Path to save the TIFF file.
    - images_data: A list of numpy arrays representing images.
    - compression_method: A single compression method for all pages.
    - custom_tags: A dictionary of custom tags to be added to the TIFF.
    """
    # Initialize a list to hold PIL Image objects
    image_objects = [Image.fromarray(image_data) for image_data in images_data]
    
    # Save the first image with the specified compression method, custom tags for all pages
    image_objects[0].save(
        output_path,
        save_all=True,
        append_images=image_objects[1:],
        compression=compression_method,
        tiffinfo=custom_tags
    )

# Ensure tmp directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Create image data for three pages
image_data1 = create_image_data(256, 256)
image_data2 = create_image_data(256, 256)
image_data3 = create_image_data(256, 256)

# List of images data
images_data = [image_data1, image_data2, image_data3]

# Choose a single compression method for all pages
compression_method = 'tiff_lzw'

# Define custom tags, including Predictor
custom_tags = {
    65000: b"\x01",  # Simplified tag definition
    317: 2,  # Tag for Predictor with value 2 indicating usage of differencing
    270: 'This is a multi-page TIFF with custom tags and differencing predictor.'  # 270 is the tag for ImageDescription
}

# Output path for the multi-page TIFF
output_path = os.path.join(output_dir, 'custom_tag_multipage_with_predictor.tiff')

# Save the multi-page TIFF
save_multipage_tiff(output_path, images_data, compression_method, custom_tags)

print(f"Multi-page TIFF saved to {output_path}")