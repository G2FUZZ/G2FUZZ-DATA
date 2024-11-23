from PIL import Image

# Create a new image with size 100x100 and color mode 'RGB'
image = Image.new('RGB', (100, 100))

# Save the image with lossless compression as a PNG file
image.save('./tmp/lossless_compression.png')