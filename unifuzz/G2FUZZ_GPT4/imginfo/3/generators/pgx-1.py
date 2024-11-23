from PIL import Image
import os

def create_pgx_image(directory='./tmp/', filename='image.pgx', size=(256, 256), color=128):
    """
    Create a PGX file containing a single-component grayscale image.

    Parameters:
    - directory: The directory to save the PGX file.
    - filename: The name of the PGX file.
    - size: A tuple (width, height) specifying the size of the image.
    - color: The grayscale color value (0-255) to fill the image.
    """
    # Ensure the target directory exists
    os.makedirs(directory, exist_ok=True)
    
    # Create a new grayscale image with the specified size and color
    img = Image.new('L', size, color)
    
    # Define the full path for the PGX file
    filepath = os.path.join(directory, filename)
    
    # Save the image in PGX format
    img.save(filepath, format='JPEG2000', quality_mode='dB', quality_layers=[80])

    print(f"PGX file saved at: {filepath}")

# Example usage
create_pgx_image()