from PIL import Image, ImageDraw
import os

# Function to create a complex multi-page TIFF
def generate_complex_multipage_tiff(image_colors=['red', 'green', 'blue'], image_size=(100, 100), tile_size=(256, 256), compression_method='jpeg', dpi=(300, 300), metadata=None, output_dir='./tmp/', output_filename='multiple_images_complex.tiff'):
    """
    Generate a complex TIFF file with customizable options such as multi-page, DPI, and metadata.
    
    Args:
    - image_colors: List of colors for the images to create a multi-page TIFF.
    - image_size: Tuple for the size of images (width, height).
    - tile_size: Tuple of (width, height) for the tile size within the TIFF.
    - compression_method: String specifying the compression method.
    - dpi: Tuple of (x dpi, y dpi) for setting the image DPI.
    - metadata: Dictionary containing metadata to include in the TIFF.
    - output_dir: Directory where the TIFF file will be saved.
    - output_filename: Filename for the saved TIFF file.
    """
    
    images = []
    for color in image_colors:
        # Create a new image with specified color
        image = Image.new('RGB', image_size, color=color)
        
        # Create a draw object (not used here but shows how to add patterns or text)
        draw = ImageDraw.Draw(image)
        # Example pattern (not drawn for solid colors): draw.rectangle([10, 10, 90, 90], fill='white')
        
        images.append(image)
    
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
                     tile=tile_size, 
                     compression=compression_method, 
                     dpi=dpi,
                     metadata=metadata)
    
    print(f"Complex TIFF file with {len(images)} pages created successfully.")

# Example usage
generate_complex_multipage_tiff(
    image_colors=['red', 'green', 'blue'],
    compression_method='jpeg',  # Note: JPEG compression might have compatibility issues.
    metadata={'Artist': 'Jane Doe', 'Description': 'A complex TIFF file with multiple colors.'}
)