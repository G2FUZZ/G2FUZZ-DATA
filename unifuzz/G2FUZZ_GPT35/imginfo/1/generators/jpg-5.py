from PIL import Image

# Create a new image with RGB mode
img = Image.new('RGB', (300, 300))

# Fill the image with a gradient pattern
pixels = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixels[i, j] = (int(255*i/img.size[0]), int(255*j/img.size[1]), 255)

# Save the image in progressive format
img.save('./tmp/progressive_rendering.jpg', 'JPEG', quality=95, progressive=True)