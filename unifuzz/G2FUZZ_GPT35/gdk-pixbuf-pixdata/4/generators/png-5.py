from PIL import Image

# Create a new image with RGB mode
image = Image.new('RGB', (300, 300))

# Fill the image with a gradient pattern
for x in range(300):
    for y in range(300):
        image.putpixel((x, y), (x, y, 255))

# Save the image with interlacing enabled
image.save('./tmp/interlaced_image.png', interlace=True)