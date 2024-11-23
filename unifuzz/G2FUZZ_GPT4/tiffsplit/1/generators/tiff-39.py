from PIL import Image, TiffImagePlugin
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Start with an empty list to hold our images
images = []

# RGB image with LZW Compression
rgb_image_lzw = Image.new("RGB", (100, 100), (0, 255, 0))  # Green square
images.append(("RGB LZW Compressed", rgb_image_lzw, "tiff_lzw"))

# CMYK image with JPEG Compression (if supported)
cmyk_color_space_jpeg = np.zeros((100, 100, 4), dtype=np.uint8)
cmyk_color_space_jpeg[:, :, 0] = 0    # Low cyan
cmyk_color_space_jpeg[:, :, 1] = 255  # High magenta
cmyk_color_space_jpeg[:, :, 2] = 0    # Low yellow
cmyk_color_space_jpeg[:, :, 3] = 0    # Low key (black)
cmyk_image_jpeg = Image.fromarray(cmyk_color_space_jpeg, 'CMYK')
images.append(("CMYK JPEG Compressed", cmyk_image_jpeg, "jpeg"))

# Grayscale image with No Compression
gray_image_no_compression = Image.new("L", (100, 100), 64)  # Darker gray square
images.append(("Grayscale No Compression", gray_image_no_compression, None))

# Function to add custom tags
def add_custom_tags(exif):
    exif[TiffImagePlugin.IMAGEDESCRIPTION] = "Example Description"
    return exif

# Save multi-page TIFF
with TiffImagePlugin.AppendingTiffWriter('./tmp/complex_structure.tiff', True) as tf:
    for name, image, compression in images:
        # Convert to byte array
        with image as img:
            if compression:
                exif = img.info.get('exif', {})
                exif = add_custom_tags(exif)
                img.save(tf, format="TIFF", compression=compression, tiffinfo=exif)
            else:
                exif = img.info.get('exif', {})
                exif = add_custom_tags(exif)
                img.save(tf, format="TIFF", tiffinfo=exif)
            tf.newFrame()