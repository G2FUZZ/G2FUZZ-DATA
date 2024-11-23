import os
import numpy as np

def create_complex_pgx_file(filename, image_data, bit_depth=8, components=1):
    """
    Creates a .pgx file from the given image data supporting multiple components and bit depths.

    Parameters:
    - filename: The path to the .pgx file to be created.
    - image_data: A numpy array containing the image pixel values. Can be 2D (grayscale) or 3D (color).
    - bit_depth: The number of bits per component.
    - components: The number of components (e.g., 1 for grayscale, 3 for RGB).
    """
    if len(image_data.shape) == 3:
        height, width, _ = image_data.shape
    else:
        height, width = image_data.shape
    
    # Define header with support for components and bit depth
    header = f"PG ML {bit_depth} {width} {height} {components}\n"
    header_bytes = bytes(header, 'ascii')

    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Write the header and image data to the file
    with open(filename, 'wb') as f:
        f.write(header_bytes)
        if components > 1:
            # Assuming the last dimension is the component dimension
            for c in range(components):
                component_data = image_data[:, :, c]
                if bit_depth == 16:
                    component_data = component_data.astype(np.uint16)
                component_data.tofile(f)
        else:
            if bit_depth == 16:
                image_data = image_data.astype(np.uint16)
            image_data.tofile(f)

# Example usage:

# Create a simple RGB image (e.g., a gradient for each color component)
width, height = 256, 256
image = np.zeros((height, width, 3), dtype=np.uint8)
image[:, :, 0] = np.linspace(0, 255, num=width*height, dtype=np.uint8).reshape((height, width)) # Red
image[:, :, 1] = np.flip(np.linspace(0, 255, num=width*height, dtype=np.uint8).reshape((height, width)), axis=0) # Green
image[:, :, 2] = np.linspace(0, 255, num=width*height, dtype=np.uint8).reshape((height, width)) // 2 # Blue

# Save the RGB image as a .pgx file with 8-bit depth for each component
create_complex_pgx_file('./tmp/complex_sample.pgx', image, bit_depth=8, components=3)