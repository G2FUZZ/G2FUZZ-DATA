from PIL import Image

# Create a new image with RGB mode
image = Image.new('RGB', (100, 100))

# Set pixel values for the image
pixels = image.load()
for i in range(image.size[0]):
    for j in range(image.size[1]):
        pixels[i, j] = (i, j, 255)  # RGB color values

# Save the image as a progressive JPEG file
image.save("./tmp/progressive_encoding.jpg", "JPEG", quality=95, optimize=True, progressive=True)