from PIL import Image

# Create a new RGB image with size 100x100
img = Image.new('RGB', (100, 100))

# Save the image as a JPG file without transparency
img.save('./tmp/opaque_image.jpg')