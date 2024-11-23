from PIL import Image

# Create a new image with RGB mode and size 100x100
image = Image.new('RGB', (100, 100))

# Set some pixels with different colors
for x in range(50):
    for y in range(50):
        image.putpixel((x, y), (255, 0, 0))  # Set pixel to red

for x in range(50, 100):
    for y in range(50, 100):
        image.putpixel((x, y), (0, 0, 255))  # Set pixel to blue

# Save the image as PNG file with lossless compression
image.save('./tmp/lossless_compression.png')