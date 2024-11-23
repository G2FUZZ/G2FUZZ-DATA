import numpy as np
from PIL import Image, TiffImagePlugin

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

def save_as_tiff_with_private_tags(image_array, file_path):
    """Saves the numpy array as a TIFF file and includes image defect data and private tags."""
    image = Image.fromarray(image_array)
    # Define custom TIFF tag for Image Defect Data
    defect_data_tag = 65000
    defect_data = "Sample defect data; adjust per image specifics."
    # Define custom TIFF tag for Private Tags
    private_tag = 65100
    private_data = "Private tag data; specific to application needs."

    # Assign the custom tags to the image info
    info = TiffImagePlugin.ImageFileDirectory_v2()
    info[defect_data_tag] = defect_data
    info[private_tag] = private_data

    # Save the image with the additional tags
    image.save(file_path, tiffinfo=info)

# Parameters for the image
width, height = 300, 300

# Generate halftone pattern
halftone_image = generate_halftone_pattern(width, height)

# Save the image with defect data and private tags
save_as_tiff_with_private_tags(halftone_image, './tmp/halftone_example_with_private_tags.tiff')

print("Halftone TIFF file with Image Defect Data and Private Tags has been saved to ./tmp/halftone_example_with_private_tags.tiff")