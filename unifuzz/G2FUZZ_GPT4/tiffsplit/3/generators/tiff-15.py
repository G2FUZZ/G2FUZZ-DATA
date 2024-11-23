import numpy as np
import os
from PIL import Image, TiffImagePlugin

# Create the ./tmp/ directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a TIFF image with specified color depth
def generate_tiff_with_color_depth_and_halftoning(filename, color_depth):
    # Generate a random image array
    if color_depth <= 8:
        # For 8-bit or lower, generate a grayscale image
        image_array = np.random.randint(0, 256, (100, 100), dtype=np.uint8)
        if color_depth < 8:
            # Adjust the scale for lower bit depths
            scale_factor = 256 // (2 ** color_depth)
            image_array = (image_array // scale_factor) * scale_factor
        mode = 'L'  # 8-bit pixels, black and white
    elif color_depth == 24:
        # For 24-bit, generate an RGB image
        image_array = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
        mode = 'RGB'
    elif color_depth == 32:
        # For 32-bit, generate an RGBA image
        image_array = np.random.randint(0, 256, (100, 100, 4), dtype=np.uint8)
        mode = 'RGBA'
    elif color_depth == 48:
        # For 48-bit, simulate by creating an RGB image with higher resolution
        image_array = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint16)
        mode = 'RGB'
    else:
        raise ValueError("Unsupported color depth")

    # Create the image
    image = Image.fromarray(image_array, mode=mode)

    # Prepare halftoning information
    # For the purpose of this example, we'll define some halftoning information.
    # In real applications, this should be replaced with actual halftoning data relevant to your image.
    halftoning_info = {
        TiffImagePlugin.IMAGEWIDTH: 100,
        TiffImagePlugin.IMAGELENGTH: 100,
        # Use numerical tag values directly
        296: 2,  # RESOLUTIONUNIT: inches
        282: TiffImagePlugin.IFDRational(300, 1),  # XRESOLUTION
        283: TiffImagePlugin.IFDRational(300, 1),  # YRESOLUTION
    }

    # Save the image with halftoning information
    image.save(filename, tiffinfo=halftoning_info)

# Generate TIFF files with various color depths and halftoning information
generate_tiff_with_color_depth_and_halftoning('./tmp/high_color_depth_8bit_halftoning.tiff', 8)
generate_tiff_with_color_depth_and_halftoning('./tmp/high_color_depth_24bit_halftoning.tiff', 24)
generate_tiff_with_color_depth_and_halftoning('./tmp/high_color_depth_32bit_halftoning.tiff', 32)
generate_tiff_with_color_depth_and_halftoning('./tmp/high_color_depth_48bit_halftoning.tiff', 48)

print("TIFF files with halftoning information have been generated and saved to ./tmp/")