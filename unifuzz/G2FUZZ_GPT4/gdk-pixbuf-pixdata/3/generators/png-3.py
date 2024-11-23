from PIL import Image
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)  # Corrected the exist_ok parameter

# Truecolor Image Creation
truecolor_image = Image.new("RGB", (100, 100), "blue")
truecolor_image.putpixel((50, 50), (255, 0, 0))  # Example of setting a pixel
truecolor_image.save("./tmp/truecolor_image.png")

# Indexed Color Image Creation
indexed_color_image = Image.new("P", (100, 100))
palette = [255, 0, 0,   0, 255, 0,   0, 0, 255]  # Define a simple palette: 3 colors - red, green, blue
indexed_color_image.putpalette(palette)  # Put palette into the image
for i in range(100):
    indexed_color_image.putpixel((i, 50), 1)  # Using the second color in the palette (green)
    indexed_color_image.putpixel((50, i), 2)  # Using the third color in the palette (blue)
indexed_color_image.save("./tmp/indexed_color_image.png")