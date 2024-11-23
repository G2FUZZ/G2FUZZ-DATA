import os
import numpy as np

def create_pgx_file(filename, image_data):
    """
    Creates a .pgx file from the given image data.

    Parameters:
    - filename: The path to the .pgx file to be created.
    - image_data: A numpy array containing the image pixel values.
    """
    height, width = image_data.shape
    bit_depth = 8  # Assuming 8-bit depth for this example

    # Define header
    # Using 'PG ML ' for big-endian as an example; adjust if needed.
    header = f"PG ML {bit_depth} {width} {height}\n"
    header_bytes = bytes(header, 'ascii')

    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Write the header and image data to the file
    with open(filename, 'wb') as f:
        f.write(header_bytes)
        image_data.tofile(f)

# Create a simple grayscale image (e.g., a gradient)
width, height = 256, 256
image = np.linspace(0, 255, num=width*height, dtype=np.uint8).reshape((height, width))

# Save the image as a .pgx file
create_pgx_file('./tmp/sample.pgx', image)