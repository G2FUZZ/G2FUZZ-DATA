from PIL import Image
import numpy as np
import os

def create_image_data(width, height):
    """Create a numpy array with random data for image creation."""
    return np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)  # Adjusted to create RGB images

def save_multipage_tiff(output_path, images_data, compression_method):
    """
    Save multiple images as a multi-page TIFF.

    Parameters:
    - output_path: Path to save the TIFF file.
    - images_data: A list of numpy arrays representing images.
    - compression_method: A single compression method for all pages.
    """
    # Initialize a list to hold PIL Image objects
    image_objects = [Image.fromarray(image_data) for image_data in images_data]
    
    # Save the first image with the specified compression method for all pages
    image_objects[0].save(
        output_path,
        save_all=True,
        append_images=image_objects[1:],
        compression=compression_method,
        tiffinfo={270: 'This is a multi-page TIFF with various compression schemes.'}  # 270 is the tag for ImageDescription
    )

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create image data for three pages
image_data1 = create_image_data(256, 256)
image_data2 = create_image_data(256, 256)
image_data3 = create_image_data(256, 256)

# List of images data
images_data = [image_data1, image_data2, image_data3]

# Choose a single compression method for all pages
compression_method = 'tiff_lzw'

# Output path for the multi-page TIFF
output_path = os.path.join(output_dir, 'complex_multipage_tiff.tiff')

# Save the multi-page TIFF
save_multipage_tiff(output_path, images_data, compression_method)

print(f"Multi-page TIFF saved to {output_path}")