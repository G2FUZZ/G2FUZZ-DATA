import numpy as np
import tifffile as tiff
import os
from skimage.color import gray2rgb

# Ensure the output directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Define image properties
image_width, image_height = 256, 256  # dimensions in pixels
bit_depth = 16  # 16 bits per pixel for detailed images
resolution = (300, 300)  # resolution in DPI (dots per inch)

# Generate a synthetic image (for demonstration, a simple gradient)
image = np.linspace(0, 2**bit_depth-1, num=image_width*image_height, dtype=np.uint16).reshape(image_height, image_width)

# Convert the grayscale image to RGB
image_rgb = gray2rgb(image.astype(np.uint8))

# Save the image as a TIFF file with specified resolutions and other metadata if needed
tiff_file_path = os.path.join(output_dir, "generated_image.tiff")

# TIFF options for compression
options = {
    'compression': 'jpeg',  # Use JPEG compression
    'jpegtables': None,     # Default JPEG tables
    'metadata': {'bit_depth': bit_depth}
}

# Adjusted call to tiff.imwrite without subsampling
tiff.imwrite(tiff_file_path, image_rgb, resolution=(resolution[0], resolution[1], 'INCH'), **options)

print(f"Generated TIFF file saved at: {tiff_file_path}")