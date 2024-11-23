from PIL import Image

# Create a new transparent image with size 200x200
image = Image.new('RGBA', (200, 200), (0, 0, 0, 0))

# Save the image as a PNG file in the specified directory
image.save('./tmp/transparent_image.png')