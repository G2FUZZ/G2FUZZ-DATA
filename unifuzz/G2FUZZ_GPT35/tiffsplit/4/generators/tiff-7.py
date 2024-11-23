from PIL import Image

# Create a new RGBA image
img = Image.new('RGBA', (100, 100), (255, 0, 0, 128))

# Save the image as a TIFF file with transparency
img.save('./tmp/transparency_example.tiff')