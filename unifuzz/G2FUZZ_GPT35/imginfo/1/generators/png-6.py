from PIL import Image

# Create a new image with RGB color and size 300x300
image = Image.new('RGB', (300, 300))

# Draw a gradient for demonstration purpose
for x in range(300):
    for y in range(300):
        image.putpixel((x, y), (x, y, 255))

# Save the image with interlacing
image.save('./tmp/interlaced_image.png', 'PNG', interlace=True)