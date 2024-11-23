from PIL import Image

# Create a new image with RGB mode
image = Image.new('RGB', (100, 100))

# Set some pixel values
for i in range(50):
    for j in range(100):
        image.putpixel((i, j), (255, 0, 0))  # Red color

# Save the image with interlacing
image.save('./tmp/interlaced_image.png', interlace=True)