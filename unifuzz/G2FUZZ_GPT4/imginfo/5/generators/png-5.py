from PIL import Image

# Define the size of the image
width, height = 100, 100

# Create a new image with a mode 'P' for palette-based and the specified size
image = Image.new('P', (width, height))

# Define a simple palette: each entry consists of (R, G, B)
# Here we define 3 colors: red, green, and blue
palette = [
    255, 0, 0,  # Red
    0, 255, 0,  # Green
    0, 0, 255,  # Blue
]

# Assign the palette to the image
image.putpalette(palette)

# Now, let's draw some simple shapes using the colors from our palette
# The '0' index in putpixel refers to the first color in the palette, and so on
for y in range(height):
    for x in range(width):
        if x < width // 3:
            image.putpixel((x, y), 0)  # Red, from our palette
        elif x < 2 * width // 3:
            image.putpixel((x, y), 1)  # Green
        else:
            image.putpixel((x, y), 2)  # Blue

# Ensure the ./tmp/ directory exists or create it
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image
image.save('./tmp/palette_image.png')

print("Palette-based image has been saved to ./tmp/palette_image.png")