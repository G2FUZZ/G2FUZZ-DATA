from PIL import Image

# Create a new transparent image
img = Image.new('RGBA', (100, 100), (0, 0, 0, 0))

# Save the image as a GIF file
img.save('./tmp/transparent_image.gif', 'GIF')