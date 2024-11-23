from PIL import Image

# Create a new image with a white background
image = Image.new('RGB', (100, 100), 'white')

# Draw a diagonal line from top left to bottom right
for i in range(100):
    image.putpixel((i, i), (0, 0, 0))

# Save the image as an interlaced GIF
image.save('./tmp/interlaced.gif', format='GIF', save_all=True, interlace=True)