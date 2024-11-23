from PIL import Image

# Create a new image (100x100 pixels) with RGB color mode
img = Image.new('RGB', (100, 100))

# Draw a diagonal line from top-left to bottom-right corner
for i in range(100):
    img.putpixel((i, i), (255, 255, 255))

# Save the image with interlacing enabled
img.save('./tmp/interlaced_image.png', interlace=True)