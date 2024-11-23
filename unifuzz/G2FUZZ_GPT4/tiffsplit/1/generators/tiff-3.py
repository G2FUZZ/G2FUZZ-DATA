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

# Create and save images with different color depths
for bitdepth in [8, 16, 32]:
    image = create_gradient_image(256, 256, bitdepth)
    filename = f'./tmp/gradient_{bitdepth}bit.tiff'
    
    # Save the image
    image.save(filename, format='TIFF', compression='tiff_deflate')

print("TIFF files have been generated.")