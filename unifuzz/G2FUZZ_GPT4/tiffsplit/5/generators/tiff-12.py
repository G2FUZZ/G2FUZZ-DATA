import numpy as np
from PIL import Image

def generate_halftone_pattern(width, height):
    """Generates a simple halftone pattern for demonstration."""
    image = np.zeros((height, width), dtype=np.uint8)

    # Create halftone patterns
    for y in range(height):
        for x in range(width):
            # Calculate intensity based on position to create a gradient
            intensity = (x + y) % width
            if intensity < width // 3:
                if (x % 3 == 0 and y % 3 == 0):
                    image[y, x] = 0
                else:
                    image[y, x] = 255
            elif intensity < 2 * (width // 3):
                if (x % 4 == 0 and y % 4 == 0) or (x % 4 == 2 and y % 4 == 2):
                    image[y, x] = 0
                else:
                    image[y, x] = 255
            else:
                if (x % 5 == 0 and y % 5 == 0):
                    image[y, x] = 0
                else:
                    image[y, x] = 255
    return image

def save_as_tiff(image_array, file_path):
    """Saves the numpy array as a TIFF file."""
    image = Image.fromarray(image_array)
    image.save(file_path)

# Parameters for the image
width, height = 300, 300

# Generate halftone pattern
halftone_image = generate_halftone_pattern(width, height)

# Save the image
save_as_tiff(halftone_image, './tmp/halftone_example.tiff')

print("Halftone TIFF file has been saved to ./tmp/halftone_example.tiff")