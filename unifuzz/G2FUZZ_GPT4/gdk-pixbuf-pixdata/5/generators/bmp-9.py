from PIL import Image, PngImagePlugin

# Define the image size and color (RGB)
width, height = 640, 480
color = (255, 0, 0)  # Red

# Create a new image with RGB mode
image = Image.new('RGB', (width, height), color)

# Metadata to embed
metadata = {
    "Author": "John Doe",
    "Software": "Python PIL",
    "Copyright": "Copyright 2023 John Doe. All rights reserved."
}

# Since BMP does not natively support extensive metadata as PNG does,
# for demonstration, we'll first save it as PNG with metadata, then convert it to BMP.
# This step is more about showing an approach rather than an effective practice for BMP files.
png_info = PngImagePlugin.PngInfo()

# Adding metadata to PNG info
for key, value in metadata.items():
    png_info.add_text(key, value)

# Save the image as PNG temporarily with metadata
tmp_png_path = './tmp/tmp_image_with_metadata.png'
image.save(tmp_png_path, pnginfo=png_info)

# Open the temporary PNG image and convert it to BMP
with Image.open(tmp_png_path) as img:
    bmp_path = './tmp/image_with_metadata.bmp'
    img.save(bmp_path)

# Cleanup: Remove the temporary PNG file
import os
os.remove(tmp_png_path)

print(f"BMP image saved at {bmp_path}")