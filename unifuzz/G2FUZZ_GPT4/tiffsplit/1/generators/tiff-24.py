from PIL import Image
import os

def generate_tiff(image_size=(800, 600), tile_size=(256, 256), compression_method='tiff_deflate', output_dir='./tmp/', output_filename='tiled_image_custom_compression.tiff'):
    """
    Generate a TIFF file with customizable compression options.
    
    Args:
    - image_size: Tuple of (width, height) for the image size.
    - tile_size: Tuple of (width, height) for the tile size within the TIFF.
    - compression_method: String specifying the compression method.
    - output_dir: Directory where the TIFF file will be saved.
    - output_filename: Filename for the saved TIFF file.
    """
    
    # Create a new image with RGB mode
    image = Image.new("RGB", image_size)
    
    # Draw some simple patterns or colors as an example
    for x in range(0, image_size[0], 100):
        for y in range(0, image_size[1], 100):
            for i in range(100):
                for j in range(100):
                    image.putpixel((x+i, y+j), (x % 255, y % 255, (x+y) % 255))
    
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Save the image in TIFF format with tiling and customizable compression
    image.save(os.path.join(output_dir, output_filename), 
               format='TIFF', 
               tile=tile_size, 
               compression=compression_method)
    
    print(f"Image saved as {output_filename} in {output_dir} with {compression_method} compression.")

# Example usage
generate_tiff(compression_method='jpeg')  # You can replace 'jpeg' with other compression methods like 'lzw', 'tiff_adobe_deflate', etc.