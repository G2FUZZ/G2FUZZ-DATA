from PIL import Image

# Create a new image with indexed color palette
image = Image.new('P', (100, 100))

# Create a palette with 256 different colors
palette = []
for i in range(256):
    palette.extend((i, i, i))  # Grayscale colors
image.putpalette(palette)

# Save the image as a GIF file
image.save('./tmp/indexed_color.gif')