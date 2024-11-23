import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an image with RGBA (Red, Green, Blue, Alpha) mode for transparency
# Size: 100x100, Color: Blue with varying transparency
image = Image.new("RGBA", (100, 100), (0, 0, 255, 0))
for x in range(100):
    for y in range(100):
        # Increasing transparency
        alpha = int((x + y) / 200 * 255)
        image.putpixel((x, y), (0, 0, 255, alpha))

# Since BMP format does not naturally support transparency, we save it first as PNG
temp_png_path = './tmp/temp_transparent_image.png'
image.save(temp_png_path)

# Re-open the PNG image and discard the alpha channel to save as BMP
# This step demonstrates handling of alpha but BMP won't retain transparency
image_without_alpha = Image.open(temp_png_path).convert("RGB")
bmp_path = './tmp/transparent_image.bmp'
image_without_alpha.save(bmp_path)

# Clean up the temporary PNG file
os.remove(temp_png_path)

print(f"Image saved at {bmp_path}")