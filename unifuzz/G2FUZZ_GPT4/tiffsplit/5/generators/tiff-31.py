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

def save_as_tiff_with_defect_data_and_min_max(image_array, file_path):
    """Saves the numpy array as a TIFF file and includes image defect data and min/max sample values."""
    image = Image.fromarray(image_array)
    # Define custom TIFF tag for Image Defect Data
    defect_data_tag = 65000
    defect_data = "Sample defect data; adjust per image specifics."
    # Define tags for Minimum and Maximum Sample Values
    min_sample_value_tag = 280  # Tag ID for MinSampleValue
    max_sample_value_tag = 281  # Tag ID for MaxSampleValue
    min_sample_value = int(np.min(image_array))
    max_sample_value = int(np.max(image_array))
    # Assign the custom tag to the image info
    info = TiffImagePlugin.ImageFileDirectory_v2()
    info[defect_data_tag] = defect_data
    info[min_sample_value_tag] = min_sample_value
    info[max_sample_value_tag] = max_sample_value
    # Save the image with the additional tags
    image.save(file_path, tiffinfo=info)

# Parameters for the image
width, height = 300, 300

# Generate halftone pattern
halftone_image = generate_halftone_pattern(width, height)

# Save the image with defect data and min/max sample values
save_as_tiff_with_defect_data_and_min_max(halftone_image, './tmp/halftone_example_with_defect_data_and_min_max.tiff')

print("Halftone TIFF file with Image Defect Data and Min/Max Sample Values has been saved to ./tmp/halftone_example_with_defect_data_and_min_max.tiff")