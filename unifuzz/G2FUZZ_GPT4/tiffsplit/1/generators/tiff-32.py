from PIL import Image, ImageDraw
import os

def generate_complex_tiff(image_sizes=[(800, 600), (400, 300)], tile_size=(256, 256), compression_method='tiff_deflate', dpi=(300, 300), metadata=None, output_dir='./tmp/', output_filename='complex_tiled_image.tiff'):
    """
    Generate a complex TIFF file with customizable options such as multi-page, DPI, and metadata.
    
    Args:
    - image_sizes: List of tuples for the sizes of images (width, height) to create a multi-page TIFF.
    - tile_size: Tuple of (width, height) for the tile size within the TIFF.
    - compression_method: String specifying the compression method.
    - dpi: Tuple of (x dpi, y dpi) for setting the image DPI.
    - metadata: Dictionary containing metadata to include in the TIFF.
    - output_dir: Directory where the TIFF file will be saved.
    - output_filename: Filename for the saved TIFF file.
    """
    
    images = []
    for size in image_sizes:
        # Create a new image with RGB mode
        image = Image.new("RGB", size)
        
        # Create a draw object to draw patterns
        draw = ImageDraw.Draw(image)
        
        # Draw some patterns or colors as an example
        for x in range(0, size[0], 100):
            for y in range(0, size[1], 100):
                color = (x % 255, y % 255, (x+y) % 255)
                # Draw rectangles instead of setting pixels one by one for efficiency
                draw.rectangle([x, y, x+99, y+99], fill=color)
        
        images.append(image)
    
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
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
                     tile=tile_size, 
                     compression=compression_method, 
                     dpi=dpi,
                     metadata=metadata)
    
    print(f"Complex TIFF image saved as {output_filename} in {output_dir} with {compression_method} compression, containing {len(image_sizes)} pages.")

# Example usage
generate_complex_tiff(
    image_sizes=[(800, 600), (400, 300)],
    compression_method='jpeg',  # You can replace 'jpeg' with other compression methods like 'lzw', 'tiff_adobe_deflate', etc.
    metadata={'Artist': 'John Doe', 'Description': 'This is a complex TIFF file.'}
)