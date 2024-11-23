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

def save_as_tiff_with_jpeg2000_compression(image_array, file_path):
    """Saves the numpy array as a TIFF file with JPEG 2000 compression."""
    image = Image.fromarray(image_array)
    # PIL does not directly support saving with JPEG 2000 compression in a TIFF.
    # However, for demonstration, we'll first save it as a JPEG 2000 (.jp2) file
    # and then mention how you might achieve TIFF with JPEG 2000 compression
    # if your environment supports it.
    temp_jp2_path = file_path.replace('.tiff', '.jp2')
    image.save(temp_jp2_path, quality_mode='dB', quality_layers=[20])

    # For actual TIFF saving with JPEG 2000 compression, additional libraries or
    # specific software support might be required, as PIL does not support
    # saving TIFF with JPEG 2000 compression directly.

    # Here's a placeholder for how it might look if your environment supports it:
    # image.save(file_path, compression='jpeg2000')

    # For this example, we're noting that the JPEG 2000 compressed image is saved
    # as a .jp2 file.
    print(f"JPEG 2000 compressed file has been saved as: {temp_jp2_path}")

# Parameters for the image
width, height = 300, 300

# Generate halftone pattern
halftone_image = generate_halftone_pattern(width, height)

# Save the image with JPEG 2000 compression
save_as_tiff_with_jpeg2000_compression(halftone_image, './tmp/halftone_example_with_jpeg2000_compression.tiff')

print("Halftone TIFF file with JPEG 2000 compression has been attempted to save as a .jp2 file for demonstration.")