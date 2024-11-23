from PIL import Image

# Create a new RGBA image with transparent background
image = Image.new('RGBA', (100, 100), (0, 0, 0, 0))

# Save the image with transparent background
image.save('./tmp/transparent_image.png')