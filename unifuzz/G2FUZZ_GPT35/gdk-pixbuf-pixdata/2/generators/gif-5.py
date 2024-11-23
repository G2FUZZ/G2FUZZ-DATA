from PIL import Image

# Create a new image with color depth of 256 colors
image = Image.new('P', (100, 100))

# Generate a palette with 256 colors
palette = []
for i in range(256):
    palette.extend((i, i, i))  # Grayscale colors

# Assign the palette to the image
image.putpalette(palette)

# Save the image
image.save('./tmp/color_depth.gif')