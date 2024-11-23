from PIL import Image, TiffImagePlugin
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Start with an empty list to hold our images
images = []

# Define image size and tile size
image_size = (800, 600)  # Width, Height

# Create a new image with RGB mode and then convert it to CMYK
image = Image.new("RGB", image_size)

# Draw some simple patterns or colors
for x in range(0, image_size[0], 100):
    for y in range(0, image_size[1], 100):
        for i in range(100):
            for j in range(100):
                image.putpixel((x+i, y+j), (x % 255, y % 255, (x+y) % 255))

# Convert the image to CMYK for the demonstration of multiple color spaces
cmyk_image = image.convert("CMYK")
images.append(("Patterned CMYK", cmyk_image, "tiff_deflate"))

# Adding more examples with different color spaces and compression
# For instance, converting the original image to grayscale and saving without compression
gray_image = image.convert("L")
images.append(("Grayscale No Compression", gray_image, None))

# Converting the original image to YCbCr with LZW compression
ycbcr_image = image.convert("YCbCr")
images.append(("YCbCr LZW Compressed", ycbcr_image, "tiff_lzw"))

# Function to add custom tags
def add_custom_tags(exif):
    exif[TiffImagePlugin.IMAGEDESCRIPTION] = "Example Description"
    return exif

# Save multi-page TIFF with images showing different patterns, color spaces, and compressions
with TiffImagePlugin.AppendingTiffWriter('./tmp/tiled_images_various.tiff', True) as tf:
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

print(f"Multi-page TIFF with various color spaces and compressions saved in ./tmp/")