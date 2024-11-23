from PIL import Image

# Create a directory for the output files if it doesn't already exist
import os
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Create a simple image for demonstration (a 100x100 red square)
image_size = (100, 100)
red_color = (255, 0, 0)
image = Image.new("RGB", image_size, red_color)

# Save the image in an uncompressed BMP format
uncompressed_filename = os.path.join(output_dir, 'uncompressed_image.bmp')
image.save(uncompressed_filename)

# Save the image in a compressed BMP format using RLE compression
# Note: As of my last update, Pillow does not directly support saving BMPs with RLE compression through a simple save option.
# RLE compression might need to be applied manually or through another library that supports BMP RLE.
# For demonstration, we save another uncompressed file but please replace this with an appropriate method or library for actual RLE compression.
compressed_filename = os.path.join(output_dir, 'compressed_image_rle_not_supported.bmp')
image.save(compressed_filename)

print(f"Files saved: {uncompressed_filename} and {compressed_filename}")