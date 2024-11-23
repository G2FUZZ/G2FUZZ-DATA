from PIL import Image

# Create a new RGB image with the specified mode and size
img = Image.new('RGB', (100, 100))

# Save the image to a file
img.save('./tmp/image.jpg')