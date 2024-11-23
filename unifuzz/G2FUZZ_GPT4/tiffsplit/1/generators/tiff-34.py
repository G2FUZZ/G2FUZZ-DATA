from PIL import Image, ImageDraw
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def create_complex_gradient_images(widths, heights, bitdepths, dpi=(300, 300), metadata=None):
    images = []
    
    for width, height, bitdepth in zip(widths, heights, bitdepths):
        # Calculate the maximum value for the given bit depth
        max_value = 2**bitdepth - 1
        
        # Create an array with values going from 0 to the maximum value for the bit depth
        gradient = np.tile(np.linspace(0, max_value, width, dtype=np.uint16 if bitdepth > 8 else np.uint8), (height, 1))
        
        # Stack the gradient arrays to create an RGB image
        image_data = np.stack((gradient,) * 3, axis=-1)
        
        if bitdepth > 8:
            # Convert the 16-bit data to 8-bit for compatibility with PIL
            image_data = (image_data / 256).astype(np.uint8)
        
        # Create an Image object from the array
        image = Image.fromarray(image_data)
        
        images.append(image)
    
    # Set default metadata if none provided
    if metadata is None:
        metadata = {
            "Software": "PIL",
            "DocumentName": "complex_gradient_images.tiff",
        }
    
    output_filename = './tmp/complex_gradient_images.tiff'
    
    # Save the images as a multi-page TIFF
    first_image = images[0]
    other_images = images[1:] if len(images) > 1 else None
    first_image.save(output_filename, 
                     save_all=True, append_images=other_images,
                     format='TIFF', 
                     compression='tiff_deflate', 
                     dpi=dpi,
                     metadata=metadata)
    
    print(f"Complex TIFF files have been generated with {len(images)} pages.")

# Create and save complex gradient images with different color depths and sizes
create_complex_gradient_images(
    widths=[256, 128, 64],
    heights=[256, 128, 64],
    bitdepths=[8, 16, 32],
    metadata={'Artist': 'John Doe', 'Description': 'These are complex gradient TIFF files.'}
)