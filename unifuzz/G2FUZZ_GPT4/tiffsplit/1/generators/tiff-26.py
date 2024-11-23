from PIL import Image

# Define image size and tile size
image_size = (800, 600)  # Width, Height
tile_size = (256, 256)   # Width, Height

# Create a new image with RGB mode and then convert it to CMYK as an example of using a different color space
image = Image.new("RGB", image_size)

# Draw some simple patterns or colors as an example
for x in range(0, image_size[0], 100):
    for y in range(0, image_size[1], 100):
        for i in range(100):
            for j in range(100):
                image.putpixel((x+i, y+j), (x % 255, y % 255, (x+y) % 255))

# Converting the image to CMYK to demonstrate the Multiple Color Spaces feature.
# Note: You can also experiment with other color spaces like 'L' for grayscale, 'YCbCr', etc.
cmyk_image = image.convert("CMYK")

# Specify the directory and filename for the TIFF
output_dir = './tmp/'
output_filename = 'tiled_image_cmyk.tiff'

# Ensure the output directory exists
import os
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save the image in TIFF format with tiling enabled and in the CMYK color space
cmyk_image.save(os.path.join(output_dir, output_filename), 
                format='TIFF', 
                tile=tile_size, 
                compression='tiff_deflate')

print(f"CMYK image saved as {output_filename} in {output_dir}")