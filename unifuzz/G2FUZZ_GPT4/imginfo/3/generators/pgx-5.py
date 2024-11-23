import os
import numpy as np

def create_pgx_file(filename, image_data):
    """
    Creates a PGX file from the given image data.
    
    Parameters:
    - filename: str. The full path to the output PGX file.
    - image_data: numpy.ndarray. 2D numpy array representing the image data.
    """
    height, width = image_data.shape
    header = f"PG ML {width} {height}\n"
    with open(filename, 'wb') as file:
        file.write(header.encode('utf-8'))  # Write the header in UTF-8 encoding
        image_data.tofile(file)  # Write the image data as raw binary

def generate_gradient_image(width, height):
    """
    Generates a simple gradient image.
    
    Parameters:
    - width: int. The width of the image.
    - height: int. The height of the image.
    
    Returns:
    - numpy.ndarray. 2D numpy array representing the generated image.
    """
    return np.tile(np.linspace(0, 255, width, dtype=np.uint8), (height, 1))

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a simple gradient image
image_data = generate_gradient_image(256, 256)

# Create a PGX file with the generated image data
create_pgx_file('./tmp/sample.pgx', image_data)

print("PGX file has been created successfully.")