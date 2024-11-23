from PIL import Image

# Create a new image with a solid color
image = Image.new('RGB', (100, 100), color='red')

# Save the image with interlacing enabled
image.save('./tmp/interlaced.gif', format='GIF', interlace=True)