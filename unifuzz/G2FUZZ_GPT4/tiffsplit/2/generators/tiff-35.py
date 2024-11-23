import numpy as np
import tifffile as tiff
import os

# Ensure the output directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Define image properties
image_width, image_height, image_depth = 256, 256, 10  # Including depth
bit_depth = 16  # 16 bits per pixel for detailed images
resolution = (300, 300)  # resolution in DPI (dots per inch)

# Generate a synthetic 3D image (for demonstration, a simple gradient along the depth)
# Each "slice" of the depth will be a gradient image, gradually changing across the depth
image = np.zeros((image_depth, image_height, image_width), dtype=np.uint16)
for z in range(image_depth):
    image[z, :, :] = np.linspace(0, 2**bit_depth - 1, num=image_width*image_height, dtype=np.uint16).reshape(image_height, image_width) * (z + 1) / image_depth

# Save the 3D image as a TIFF file with specified resolutions and additional depth information
tiff_file_path = os.path.join(output_dir, "generated_image_with_depth.tiff")
tiff.imwrite(tiff_file_path, image, resolution=resolution, metadata={'axes': 'ZYX'})

print(f"Generated TIFF file with depth saved at: {tiff_file_path}")