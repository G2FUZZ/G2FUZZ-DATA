from PIL import Image

# Create a new RGB image
img = Image.new('RGB', (100, 100))

# Set pixel data for the image
pixels = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixels[i, j] = (255, 255, 255)  # Set all pixels to white

# Save the image with progressive encoding
img.save('./tmp/progressive_encoding.jpg', format='JPEG', quality=95, optimize=True, progressive=True)