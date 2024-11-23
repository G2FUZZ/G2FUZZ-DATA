from PIL import Image

# Create a new image with RGB mode
image = Image.new('RGB', (100, 100))

# Save the image with specified compression level
image.save('./tmp/compressed_image.png', compress_level=9)