from PIL import Image

# Create a new RGBA image
img = Image.new('RGBA', (200, 200))

# Create a red rectangle with 50% transparency
red_layer = Image.new('RGBA', (100, 100), (255, 0, 0, 128))
img.paste(red_layer, (0, 0))

# Create a green circle with 75% transparency
green_layer = Image.new('RGBA', (100, 100), (0, 255, 0, 191))
img.paste(green_layer, (100, 0), mask=green_layer)

# Create a blue triangle with 25% transparency
blue_layer = Image.new('RGBA', (100, 100), (0, 0, 255, 64))
img.paste(blue_layer, (50, 50), mask=blue_layer)

# Save the image as a TIFF file with multiple layers and transparency
img.save('./tmp/complex_transparency_example.tiff')