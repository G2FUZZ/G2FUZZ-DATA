import numpy as np
import tifffile as tiff
import os

def generate_gradient_image(width, height, bit_depth):
    """Generates a gradient image from black to white."""
    return np.linspace(0, 2**bit_depth-1, num=width*height, dtype=np.uint16).reshape(height, width)

def generate_random_noise_image(width, height, bit_depth):
    """Generates a random noise image."""
    return np.random.randint(0, 2**bit_depth, size=(height, width), dtype=np.uint16)

def generate_solid_color_image(width, height, bit_depth, color_value):
    """Generates a solid color image."""
    image = np.full((height, width), fill_value=color_value, dtype=np.uint16)
    return image

def save_multi_page_tiff(file_path, images, resolution=(300, 300), metadata=None):
    """Saves multiple images as a multi-page TIFF file."""
    with tiff.TiffWriter(file_path, bigtiff=True) as tif:
        for img in images:
            tif.write(img, resolution=resolution, metadata=metadata)

# Ensure the output directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Define image properties
image_width, image_height = 256, 256  # dimensions in pixels
bit_depth = 16  # 16 bits per pixel

# Generate different types of images for demonstration
gradient_image = generate_gradient_image(image_width, image_height, bit_depth)
random_noise_image = generate_random_noise_image(image_width, image_height, bit_depth)
solid_color_image = generate_solid_color_image(image_width, image_height, bit_depth, color_value=2**bit_depth//2)

# List of images to save in the TIFF file
images = [gradient_image, random_noise_image, solid_color_image]

# Save the images as a multi-page TIFF file
tiff_file_path = os.path.join(output_dir, "complex_structure_image.tiff")
save_multi_page_tiff(tiff_file_path, images, resolution=(300, 300), metadata={'bit_depth': bit_depth})

print(f"Generated multi-page TIFF file saved at: {tiff_file_path}")