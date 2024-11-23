from PIL import Image

# Create a new image
img = Image.new('RGB', (100, 100))

# Save the image with progressive scanning
img.save("./tmp/progressive.jpg", format='JPEG', quality=95, optimize=True, progressive=True)