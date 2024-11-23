from PIL import Image

# Create a new image with RGBA mode
img = Image.new('RGBA', (100, 100), (255, 0, 0, 255))

# Create a new layer by adding a green rectangle
layer = Image.new('RGBA', (100, 100), (0, 255, 0, 128))

# Composite the new layer on top of the original image
img = Image.alpha_composite(img, layer)

# Save the image with layers as a TIFF file
img.save('./tmp/multi_layer_image.tiff')