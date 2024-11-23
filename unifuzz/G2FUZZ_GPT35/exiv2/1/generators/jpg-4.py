from PIL import Image

# Create a new image with RGB mode
image = Image.new('RGB', (100, 100))

# Set some pixels with random colors
for x in range(100):
    for y in range(100):
        image.putpixel((x, y), (x, y, x+y))

# Save the image as a progressive jpg file
image.save("./tmp/progressive_loading.jpg", format="JPEG", quality=95, optimize=True, progressive=True)