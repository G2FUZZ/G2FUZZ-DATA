from PIL import Image, ImageDraw

# Create a new image with limited color palette
img = Image.new('P', (100, 100))
draw = ImageDraw.Draw(img)

# Define a color palette with 256 colors
palette = []
for i in range(256):
    palette.extend((i, i, i))  # grayscale colors

# Assign the palette to the image
img.putpalette(palette)

# Draw a rectangle on the image
draw.rectangle([20, 20, 80, 80], fill=128)

# Save the image as a GIF file
img.save('./tmp/limited_color_palette.gif', 'GIF')