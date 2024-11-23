import numpy as np
import tifffile as tiff
import os

# Create a directory for saving the generated TIFF files if it doesn't exist
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Helper function to generate resolution info for TIFF
def generate_res_info(dpi):
    # Convert DPI to pixels per centimeter, TIFF uses centimeters
    res = dpi * 2.54 / 10
    return (int(res), int(res))

# Generate an image with an alpha channel
# For demonstration, let's create a 200x200 image with 4 channels (RGBA)
width, height = 200, 200
channels = 4  # RGBA, where A is the alpha channel

# Create an array filled with random values for RGB and set the alpha channel to a specific value (e.g., 128 for 50% transparency)
image_data_rgba = np.random.randint(0, 256, (height, width, channels), dtype=np.uint8)
image_data_rgba[:, :, 3] = 128  # Set the alpha channel to 128 (50% transparency)
rgba_res = generate_res_info(300)  # 300 DPI for RGBA image

# Generate a grayscale image with a different size and resolution
gray_width, gray_height = 100, 100
gray_image_data = np.random.randint(0, 256, (gray_height, gray_width), dtype=np.uint8)
gray_res = generate_res_info(150)  # 150 DPI for grayscale image

# Prepare metadata
metadata = {
    "Artist": "Python tifffile",
    "Software": "tifffile",
    "Description": "Multi-page TIFF with RGBA and grayscale images"
}

# Save TIFF with multiple images, resolutions, and metadata
tiff_filename = os.path.join(output_dir, "complex_structure.tiff")
tiff.imwrite(
    tiff_filename,
    image_data_rgba,
    resolution=(rgba_res[0], rgba_res[1], 'CENTIMETER'),
    metadata={'description': metadata["Description"], 'artist': metadata["Artist"], 'software': metadata["Software"]},
    subifds=1
)

# Append the grayscale image as a new page to the TIFF
with tiff.TiffWriter(tiff_filename, append=True) as tif:
    tif.write(
        gray_image_data,  # Corrected variable name
        resolution=(gray_res[0], gray_res[1], 'CENTIMETER'),
        metadata={'description': metadata["Description"]}
    )

print(f"Multi-page TIFF file saved to {tiff_filename}")