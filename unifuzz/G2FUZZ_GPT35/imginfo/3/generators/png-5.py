from PIL import Image

# Create a new image with RGB mode
img = Image.new('RGB', (100, 100), color = 'white')

# Save the image as an interlaced PNG file
img.save('./tmp/interlaced.png', interlace=True)