import numpy as np
import os

def generate_pixel_matrix(width, height):
    """
    Generate a simple gradient pixel matrix.
    Each pixel value will be a grayscale value from 0 to 255.
    """
    # Initialize an empty array for the pixel data
    pixel_matrix = np.zeros((height, width), dtype=np.uint8)
    
    # Create a vertical gradient
    for y in range(height):
        for x in range(width):
            pixel_matrix[y, x] = (x + y) % 256  # Example pattern
    
    return pixel_matrix

def save_pixel_matrix_to_file(pixel_matrix, file_path):
    """
    Save the pixel matrix to a file.
    """
    # Ensure the target directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Save the pixel data
    with open(file_path, 'wb') as file:
        for row in pixel_matrix:
            file.write(bytes(row))

# Define image dimensions
width, height = 256, 256

# Generate pixel matrix
pixel_matrix = generate_pixel_matrix(width, height)

# File path to save the pixel data
file_path = './tmp/gradient_image.pixdata'

# Save the pixel matrix to a file
save_pixel_matrix_to_file(pixel_matrix, file_path)

print(f"Pixel data saved to {file_path}")