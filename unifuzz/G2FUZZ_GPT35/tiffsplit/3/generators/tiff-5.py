from PIL import Image

# Create a new RGBA image with transparency
image = Image.new('RGBA', (100, 100), (255, 0, 0, 128))

# Save the image as a TIFF file with transparency
image.save('./tmp/transparency.tiff')