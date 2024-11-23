from PIL import Image

# Create a new RGBA image with transparency support
img = Image.new('RGBA', (100, 100), (255, 0, 0, 128))

# Save the image with transparency as a PNG file
img.save('./tmp/transparency_example.png', 'PNG')