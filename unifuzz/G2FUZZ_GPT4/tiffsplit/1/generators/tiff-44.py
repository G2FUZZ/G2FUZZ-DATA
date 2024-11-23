from PIL import Image, ImageDraw
import os

def generate_complex_tiff(image_sizes=[(800, 600), (400, 300), (200, 150)], 
                          tile_size=(256, 256), 
                          compression_method='tiff_deflate', 
                          dpi_settings=[(300, 300), (150, 150), (72, 72)], 
                          output_dir='./tmp/', 
                          output_filename='multi_page_tiff.tiff'):
    """
    Generate a TIFF file with multiple pages, each with different sizes and DPI settings.
    
    Args:
    - image_sizes: List of tuples for the sizes of each page (width, height).
    - tile_size: Tuple of (width, height) for the tile size within the TIFF.
    - compression_method: String specifying the compression method.
    - dpi_settings: List of tuples for the DPI settings of each page (x_dpi, y_dpi).
    - output_dir: Directory where the TIFF file will be saved.
    - output_filename: Filename for the saved TIFF file.
    """
    
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_path = os.path.join(output_dir, output_filename)
    
    # Initialize an empty list to hold the images
    images = []
    
    for idx, size in enumerate(image_sizes):
        # Create a new image with RGB mode for each size
        image = Image.new("RGB", size)
        draw = ImageDraw.Draw(image)
        
        # Draw some patterns or colors to distinguish between pages
        for x in range(0, size[0], 100):
            for y in range(0, size[1], 100):
                draw.rectangle([x, y, x+50, y+50], fill=(x % 255, y % 255, (x+y) % 255))
        
        # Append the image to the list, along with its DPI setting
        images.append(image)
    
    # Save the first image with the save_all parameter to create a multi-page TIFF
    images[0].save(output_path, 
                   save_all=True, 
                   append_images=images[1:], 
                   format='TIFF', 
                   tile=tile_size, 
                   compression=compression_method, 
                   dpi=dpi_settings[0])
    
    # Update the DPI for the subsequent images
    for idx, image in enumerate(images[1:], start=1):
        image.save(output_path, dpi=dpi_settings[idx], append_images=[image])
    
    print(f"Multi-page TIFF saved as {output_filename} in {output_dir} with {compression_method} compression.")

# Example usage
generate_complex_tiff(compression_method='lzw')  # You can replace 'lzw' with other compression methods like 'jpeg', 'tiff_adobe_deflate', etc.