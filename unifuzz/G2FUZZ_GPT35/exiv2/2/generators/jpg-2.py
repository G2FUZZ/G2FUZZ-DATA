from PIL import Image

# Create a new RGB image
image = Image.new('RGB', (100, 100))

# Save the image as a JPEG file
image.save('./tmp/color_space.jpg', 'JPEG')