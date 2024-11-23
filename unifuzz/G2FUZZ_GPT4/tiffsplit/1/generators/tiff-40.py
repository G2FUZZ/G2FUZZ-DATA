from PIL import Image, ImageDraw
import numpy as np
import os

def generate_complex_rgb_tiff(image_sizes=[(100, 100)], tile_size=(256, 256), compression_method='tiff_deflate', dpi=(300, 300), metadata=None, output_dir='./tmp/', output_filename='complex_rgb_image_subsampling.tiff'):
    """
    Generate a complex TIFF file with customizable options such as multi-page, DPI, metadata, and support for subsampling and planar configuration.
    
    Args:
    - image_sizes: List of tuples for the sizes of images (width, height) to create a multi-page TIFF.
    - tile_size: Tuple of (width, height) for the tile size within the TIFF.
    - compression_method: String specifying the compression method.
    - dpi: Tuple of (x dpi, y dpi) for setting the image DPI.
    - metadata: Dictionary containing metadata to include in the TIFF.
    - output_dir: Directory where the TIFF file will be saved.
    - output_filename: Filename for the saved TIFF file.
    """
    
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    images = []
    for size in image_sizes:
        # Generate an RGB image
        image = Image.new("RGB", size, (255, 255, 0))  # Yellow square
        
        # Save as JPEG with subsampling as a temporary step
        jpeg_temp_path = os.path.join(output_dir, 'temp_subsampling.jpg')
        image.save(jpeg_temp_path, quality=95, subsampling=0)  # '0' corresponds to '4:4:4'
        
        # Read the JPEG image back with subsampling applied
        jpeg_image_with_subsampling = Image.open(jpeg_temp_path)
        
        images.append(jpeg_image_with_subsampling)
        
        # Clean up the temporary JPEG file
        os.remove(jpeg_temp_path)
    
    # Set default metadata if none provided
    if metadata is None:
        metadata = {
            "Software": "PIL",
            "DocumentName": output_filename,
        }
    
    # Save the images as a multi-page TIFF
    first_image = images[0]
    other_images = images[1:]  # This will be an empty list if there's only one image, which is fine

    first_image.save(os.path.join(output_dir, output_filename), 
                     save_all=True, append_images=other_images,
                     format='TIFF', 
                     tile=tile_size, 
                     compression=compression_method, 
                     dpi=dpi,
                     metadata=metadata)
    
    print(f"Complex RGB TIFF image saved as {output_filename} in {output_dir} with {compression_method} compression, containing {len(image_sizes)} pages.")

# Example usage
generate_complex_rgb_tiff(
    image_sizes=[(100, 100)],
    compression_method='tiff_deflate',
    metadata={'Artist': 'Jane Doe', 'Description': 'This is a complex RGB TIFF file with subsampling.'}
)