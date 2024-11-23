from PIL import Image, ImageDraw
import os

# Function to create a simple image with a specified color
def create_image_with_color(color, size=(100, 100), dpi=(300, 300)):
    image = Image.new("RGB", size, color)
    draw = ImageDraw.Draw(image)
    draw.text((10, 40), f"Layer {color}", fill="white")
    image.info['dpi'] = dpi
    return image

# Creating a list of images with different colors
colors = ['red', 'green', 'blue', 'yellow']
images = [create_image_with_color(color, dpi=(300, 300)) for color in colors]

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Save the images as a multi-page TIFF with LZW compression and DPI setting
images[0].save(
    './tmp/multi_page_advanced.tiff',
    save_all=True,
    append_images=images[1:],
    compression="tiff_lzw",
    dpi=(300, 300)
)

print("Advanced multi-page TIFF has been saved in ./tmp/multi_page_advanced.tiff")