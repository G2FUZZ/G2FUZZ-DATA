from PIL import Image

# Create a new image with RGB mode
image = Image.new('RGB', (100, 100))

# Set some pixels to create a simple image
for x in range(50):
    for y in range(50):
        image.putpixel((x, y), (255, 0, 0))  # Red

# Save the image in progressive format
image.save('./tmp/progressive_image.jpg', format='JPEG', quality=95, optimize=True, progressive=True)