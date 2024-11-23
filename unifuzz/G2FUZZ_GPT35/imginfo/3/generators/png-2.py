from PIL import Image

# Create a new RGBA image with transparency
img = Image.new('RGBA', (100, 100), (0, 0, 0, 0))

# Save the image to a file
img.save('./tmp/transparent_image.png')