from PIL import Image, ImageDraw
import numpy as np
import os

def generate_complex_gradient_tiff(image_sizes=[(256, 256), (128, 128)], compression_method='tiff_lzw', dpi=(300, 300), metadata=None, output_dir='./tmp/', output_filename='complex_gradient_tiff.tiff'):
    """
    Generate a complex TIFF file with gradients on each page, customizable options such as multi-page, DPI, and metadata.
    
    Args:
    - image_sizes: List of tuples for the sizes of images (width, height) to create a multi-page TIFF.
    - compression_method: String specifying the compression method.
    - dpi: Tuple of (x dpi, y dpi) for setting the image DPI.
    - metadata: Dictionary containing metadata to include in the TIFF.
    - output_dir: Directory where the TIFF file will be saved.
    - output_filename: Filename for the saved TIFF file.
    """
    
    images = []
    for size in image_sizes:
        width, height = size
        image = np.zeros((height, width), dtype=np.uint8)
        
        # Creating a gradient effect for our image
        for i in range(height):
            for j in range(width):
                image[i, j] = (i+j) % 256
        
        # Convert the numpy array to a PIL image and append to the list
        img = Image.fromarray(image)
        images.append(img)
    
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Set default metadata if none provided
    if metadata is None:
        metadata = {
            "Software": "PIL",
            "DocumentName": output_filename,
        }
    
    # Save the images as a multi-page TIFF
    first_image = images[0]
    other_images = images[1:] if len(images) > 1 else None
    first_image.save(os.path.join(output_dir, output_filename), 
                     save_all=True, append_images=other_images,
                     format='TIFF', 
                     compression=compression_method, 
                     dpi=dpi,
                     metadata=metadata)
    
    print(f"Complex gradient TIFF image saved as {output_filename} in {output_dir} with {compression_method} compression, containing {len(image_sizes)} pages.")

# Example usage
generate_complex_gradient_tiff(
    image_sizes=[(256, 256), (128, 128)],
    compression_method='tiff_lzw',
    metadata={'Artist': 'Jane Doe', 'Description': 'This is a complex gradient TIFF file.'}
)