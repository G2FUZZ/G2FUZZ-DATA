from PIL import Image

# Create a new image with RGB mode
image = Image.new('RGB', (200, 200))

# Set the pixels of the image to create a gradient pattern
pixels = image.load()
for i in range(200):
    for j in range(200):
        pixels[i, j] = (i, j, 255)  # Gradient pattern from blue to white

# Save the image as an interlaced GIF file with a more complex gradient pattern
image.save('./tmp/complex_interlaced.gif', format='GIF', save_all=True, interlace=True)