from PIL import Image

# Create a new image with RGB color
image = Image.new('RGB', (100, 100))

# Save the image as a PNG file
image.save('./tmp/lossless_compression.png')