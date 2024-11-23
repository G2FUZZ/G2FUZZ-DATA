from PIL import Image

# Create a new image with RGBA mode (4 layers: Red, Green, Blue, Alpha)
image = Image.new('RGBA', (100, 100))

# Save the image with layers as a TIFF file
image.save('./tmp/multi_layer_image.tiff', format='TIFF')