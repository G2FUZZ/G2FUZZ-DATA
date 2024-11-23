import os
from PIL import Image

# Create the target directory if it doesn't exist
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the width and height of the image
width, height = 100, 100

# Create a new 8-bit palette image
image = Image.new("P", (width, height))

# Define a simple palette: 3 colors, black, red, and green
palette = [
    0, 0, 0,  # black
    255, 0, 0,  # red
    0, 255, 0,  # green
] + [0, 0, 0] * 253  # Fill the rest of the 256 color slots with black

# Set the palette of the image
image.putpalette(palette)

# Draw a simple pattern using the palette colors
for y in range(height):
    for x in range(width):
        if x < width // 3:
            color = 0  # Use the first color from the palette (black)
        elif x < 2 * width // 3:
            color = 1  # Use the second color from the palette (red)
        else:
            color = 2  # Use the third color from the palette (green)
        image.putpixel((x, y), color)

# Save the image
image_path = os.path.join(output_dir, 'palette_example.bmp')
image.save(image_path, 'BMP')

print(f"Image saved to {image_path}")