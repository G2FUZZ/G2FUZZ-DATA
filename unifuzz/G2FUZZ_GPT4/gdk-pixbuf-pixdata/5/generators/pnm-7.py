import os
import numpy as np

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def create_pnm_image(filename, width, height, image_type='P3'):
    """
    Creates a simple PNM image with basic patterns. It supports P3 (PPM) format for demonstration.
    
    :param filename: The file name where the image will be saved.
    :param width: Width of the image.
    :param height: Height of the image.
    :param image_type: Type of the PNM image. Default is 'P3' for PPM.
    """
    # Create an array to hold the image data
    data = np.zeros((height, width, 3), dtype=np.uint8)

    # Fill the image with a gradient pattern
    for y in range(height):
        for x in range(width):
            data[y, x, 0] = (x + y) % 256  # Red channel
            data[y, x, 1] = (x * 2) % 256  # Green channel
            data[y, x, 2] = (y * 2) % 256  # Blue channel
            
    # Convert the array to a PNM format string
    if image_type.upper() == 'P3':
        header = f'{image_type}\n{width} {height}\n255\n'
        body = '\n'.join(' '.join(str(val) for val in row.ravel()) for row in data)
        pnm_data = header + body
    else:
        raise ValueError("Unsupported image type. Only 'P3' (PPM) is supported in this example.")
    
    # Save the PNM data to a file
    with open(filename, 'w') as file:
        file.write(pnm_data)

# Example usage
create_pnm_image('./tmp/example.ppm', 100, 100)