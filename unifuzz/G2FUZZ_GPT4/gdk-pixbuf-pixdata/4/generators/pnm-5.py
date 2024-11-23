import os
import numpy as np

# Create the 'tmp' directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a simple RGB image with no alpha channel
def generate_rgb_image(width, height, color):
    """
    Generates a simple RGB image as a numpy array.

    Parameters:
    - width: Width of the image.
    - height: Height of the image.
    - color: A tuple of (R, G, B) specifying the color.

    Returns:
    - A numpy array representing an RGB image.
    """
    # Create an array filled with the color. Shape: (height, width, 3)
    image = np.full((height, width, 3), color, dtype=np.uint8)
    return image

# Function to save the RGB image as a PNM file
def save_as_pnm(image, file_path):
    """
    Saves an RGB image as a PNM file.

    Parameters:
    - image: A numpy array representing an RGB image.
    - file_path: The path where the PNM file will be saved.
    """
    height, width, _ = image.shape
    # Open the file in binary write mode
    with open(file_path, 'wb') as f:
        # Write the P6 header, width, height, and max color value
        f.write(f'P6\n{width} {height}\n255\n'.encode())
        # Write the image data
        f.write(image.tobytes())

# Generate an example RGB image
color = (255, 0, 0)  # Red
width, height = 100, 100
image = generate_rgb_image(width, height, color)

# Save the image as a PNM file
file_path = './tmp/example_image.pnm'
save_as_pnm(image, file_path)

print(f"RGB image saved as {file_path}")