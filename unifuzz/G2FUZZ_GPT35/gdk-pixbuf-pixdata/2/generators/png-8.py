from PIL import Image

# Create a new RGB image
img = Image.new('RGB', (100, 100), color = 'white')

# Interlace the image
img.save('./tmp/interlaced_image.png', interlace=True)