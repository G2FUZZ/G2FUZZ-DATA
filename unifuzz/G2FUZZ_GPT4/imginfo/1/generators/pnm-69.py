import numpy as np
import os

def create_complex_pnm_image(filename, width, height, maxval=255):
    """
    Create a complex PNM image with patterns, shapes, and save it to filename.
    """
    # Ensure the tmp directory exists
    os.makedirs('./tmp/', exist_ok=True)
    filepath = os.path.join('./tmp/', filename)

    # Initialize an empty image
    img = np.zeros((height, width, 3), dtype=np.uint8)

    # Draw complex patterns and shapes
    # Gradient Background
    for i in range(height):
        for j in range(width):
            img[i, j] = [(i / height) * maxval, (j / width) * maxval, ((i + j) / (width + height)) * maxval]

    # Circle
    center_x, center_y = width // 4, height // 4
    radius = min(width, height) // 10
    for i in range(height):
        for j in range(width):
            if ((center_x - j) ** 2 + (center_y - i) ** 2) <= radius ** 2:
                img[i, j] = [maxval, 0, 0]  # red circle

    # Rectangle
    top_left_x, top_left_y = 3 * width // 4, 3 * height // 4
    rect_width, rect_height = width // 5, height // 10
    img[top_left_y:top_left_y + rect_height, top_left_x:top_left_x + rect_width] = [0, maxval, 0]  # green rectangle

    # Write PPM header
    with open(filepath, 'wb') as f:
        f.write(bytearray(f"P6\n{width} {height}\n{maxval}\n", 'ascii'))

        # Flatten the image array and write the binary data
        img.tofile(f)

# Example usage
create_complex_pnm_image('complex_example.ppm', 256, 256)