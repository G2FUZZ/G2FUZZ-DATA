from PIL import Image

# Create a new image with RGB mode
image = Image.new('RGB', (100, 100))

# Set the pixels of the image to create a simple pattern
pixels = image.load()
for i in range(100):
    for j in range(100):
        if (i+j) % 20 == 0:
            pixels[i, j] = (255, 0, 0)  # Red pixels

# Save the image as an interlaced GIF file
image.save('./tmp/interlaced.gif', format='GIF', save_all=True, interlace=True)