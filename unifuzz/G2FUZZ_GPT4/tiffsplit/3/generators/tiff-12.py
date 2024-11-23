from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image for demonstration (e.g., 100x100 pixels, red)
width, height = 100, 100
color = (255, 0, 0, 255)  # Red color in RGBA format
image = Image.new("RGBA", (width, height), color)

# Save the image in TIFF format (without specifying byte order, as it's not supported directly)
little_endian_file = './tmp/little_endian.tif'
image.save(little_endian_file, format='TIFF')

big_endian_file = './tmp/big_endian.tif'
image.save(big_endian_file, format='TIFF')

print(f"Saved TIFF to {little_endian_file}")
print(f"Saved TIFF to {big_endian_file}")