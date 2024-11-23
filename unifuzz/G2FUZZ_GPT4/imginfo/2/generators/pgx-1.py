import os
import numpy as np

def create_grayscale_gradient(width, height):
    """Create a grayscale gradient image of given dimensions."""
    # Create an array filled with a gradient from 0 to 255 (8-bit grayscale values)
    gradient = np.tile(np.linspace(0, 255, width, dtype=np.uint8), (height, 1))
    return gradient

def save_pgx(image, filename):
    """Save a grayscale image as a PGX file."""
    if not os.path.exists('./tmp/'):
        os.makedirs('./tmp/')
    with open(filename, 'wb') as f:
        # Assuming the simplest form of PGX as raw pixel data
        # For a real implementation, header or specific formatting may be required
        img_data = image.astype(np.uint8)
        img_data.tofile(f)

# Example usage
width, height = 256, 256  # Width and height of the image
gradient_image = create_grayscale_gradient(width, height)
save_pgx(gradient_image, './tmp/gradient.pgx')

print("PGX file saved successfully.")