import numpy as np
import os
from PIL import Image, TiffImagePlugin

# Create a directory for saving the generated TIFF files if it doesn't exist
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

images = []

# Generate an image with an alpha channel
width, height = 100, 100
channels = 4  # RGBA, where A is the alpha channel
image_data = np.random.randint(0, 256, (height, width, channels), dtype=np.uint8)
image_data[:, :, 3] = 128  # Set the alpha channel to 128 (50% transparency)
rgba_image = Image.fromarray(image_data)
images.append(("RGBA Image", rgba_image, None))  # No specific compression for RGBA

# Adding Spot Color Support
spot_color_channel = np.zeros((height, width), dtype=np.uint8) + 150  # A specific shade of blue
extended_image_data = np.dstack((image_data[:, :, :3], spot_color_channel))  # Ignore the alpha for spot color simulation
spot_color_image = Image.fromarray(extended_image_data)
images.append(("Spot Color Image", spot_color_image, "tiff_adobe_deflate"))  # Using Adobe Deflate compression for spot color image

# Function to add custom tags
def add_custom_tags(exif):
    exif[TiffImagePlugin.IMAGEDESCRIPTION] = "Example Description with Alpha and Spot Color"
    return exif

# Save multi-page TIFF
multi_page_tiff_filename = os.path.join(output_dir, "combined_image.tiff")
with TiffImagePlugin.AppendingTiffWriter(multi_page_tiff_filename, True) as tf:
    for name, image, compression in images:
        with image as img:
            exif = img.info.get('exif', {})
            exif = add_custom_tags(exif)
            if compression:
                img.save(tf, format="TIFF", compression=compression, tiffinfo=exif)
            else:
                img.save(tf, format="TIFF", tiffinfo=exif)
            tf.newFrame()

print(f"Multi-page TIFF file saved to {multi_page_tiff_filename}")