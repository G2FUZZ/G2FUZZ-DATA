from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def create_gradient_image(width, height, bitdepth):
    # Calculate the maximum value for the given bit depth
    max_value = 2**bitdepth - 1
    
    # Create an array with values going from 0 to the maximum value for the bit depth
    gradient = np.tile(np.linspace(0, max_value, width, dtype=np.uint16 if bitdepth > 8 else np.uint8), (height, 1))
    
    # Stack the gradient arrays to create an RGB image
    image_data = np.stack((gradient,) * 3, axis=-1)
    
    if bitdepth > 8:
        # Convert the 16-bit data to 8-bit for compatibility with PIL
        # This step involves scaling down the data, which loses some of the high bit depth's advantages
        image_data = (image_data / 256).astype(np.uint8)
    
    # Create an Image object from the array
    image = Image.fromarray(image_data)
    
    return image

# Function to determine if BigTIFF extension is needed based on the image size
def needs_bigtiff_extension(width, height, bitdepth):
    # Estimate file size in bytes (width * height * bits_per_channel * number_of_channels / 8)
    # Note: This is a simplified estimation, actual file size may vary due to metadata, compression, etc.
    estimated_file_size = width * height * bitdepth * 3 / 8
    # 4GB in bytes is the limit for standard TIFF, above which BigTIFF is recommended
    return estimated_file_size > 4 * 1024**3

# Create and save images with different color depths
for bitdepth in [8, 16, 32]:
    image = create_gradient_image(256, 256, bitdepth)
    filename = f'./tmp/gradient_{bitdepth}bit.tiff'
    
    # Check if BigTIFF extension is needed
    if needs_bigtiff_extension(256, 256, bitdepth):
        # Save the image with BigTIFF extension
        # Note: As of my last update, PIL/Pillow does not directly support BigTIFF. This would typically require
        # a library that supports BigTIFF, such as libtiff or a manual implementation.
        # For demonstration purposes, this will mimic the parameter change for BigTIFF support.
        # You would need to use a library or method that supports BigTIFF to actually generate one.
        print(f"BigTIFF would be used for {filename}. However, PIL/Pillow does not support BigTIFF natively.")
    else:
        # Save the image normally as TIFF
        image.save(filename, format='TIFF', compression='tiff_deflate')

print("TIFF files have been generated, with consideration for BigTIFF extension where applicable.")