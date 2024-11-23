from PIL import Image

# Create a new image with a color palette
image = Image.new('P', (100, 100))
palette = []
for i in range(256):
    palette.extend((i, i, i))  # grayscale palette
image.putpalette(palette)

# Save the image as a gif file
image.save('./tmp/grayscale_palette.gif')