import numpy as np
import tifffile as tiff
import os

def create_gradient_image(width, height, channels=4):
    """Create an RGBA image with a gradient effect."""
    image = np.zeros((height, width, channels), dtype=np.uint8)
    for x in range(width):
        for y in range(height):
            image[y, x] = [x % 256, y % 256, (x+y) % 256, 255]  # RGBA
    return image

def add_metadata(image, description="Gradient Image"):
    """Add metadata to an image."""
    metadata = {'ImageDescription': description}
    return image, metadata

def save_multipage_tiff(path, images, compressions):
    """Save images as a multi-page TIFF with different compression algorithms."""
    with tiff.TiffWriter(path, bigtiff=False) as tiff_writer:
        for image, compression in zip(images, compressions):
            # Remove the alpha channel if present (assuming the last channel is alpha)
            if image.shape[2] == 4:
                image = image[:, :, :3]  # Keep only the first three channels (RGB)
            image, metadata = add_metadata(image)
            tiff_writer.write(image, compression=compression, metadata=metadata)

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Define image dimensions and create images
width, height = 256, 256
images = [create_gradient_image(width, height) for _ in range(3)]  # Create 3 images

# Define compression algorithms for each image
compressions = ['none', 'jpeg', 'deflate']

# Save the images as a multi-page TIFF file
output_path = os.path.join(output_dir, 'complex_image_with_alpha.tiff')
save_multipage_tiff(output_path, images, compressions)

print(f"Multi-page TIFF file with different compressions has been saved to {output_path}")