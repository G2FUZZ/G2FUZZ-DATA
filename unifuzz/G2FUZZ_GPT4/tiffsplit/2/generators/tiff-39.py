import numpy as np
import tifffile as tiff
import os

# Ensure the output directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Define image properties
image_width, image_height = 256, 256  # dimensions in pixels
bit_depth = 16  # 16 bits per pixel for detailed images
resolution = (300, 300)  # resolution in DPI (dots per inch)

# Generate a synthetic image (for demonstration, a simple gradient)
# Note: The actual range and values can be adjusted based on the bit depth and desired image content
image = np.linspace(0, 2**bit_depth-1, num=image_width*image_height, dtype=np.uint16).reshape(image_height, image_width)

# Define software and artist tags
software = "Custom Image Generator 1.0"
artist = "John Doe"

# Save the image as a TIFF file with specified resolutions and other metadata including Software and Artist Tags
tiff_file_path = os.path.join(output_dir, "generated_image_with_tags.tiff")
tiff.imwrite(tiff_file_path, image, resolution=resolution, metadata={'bit_depth': bit_depth, 'Software': software, 'Artist': artist})

print(f"Generated TIFF file with tags saved at: {tiff_file_path}")