from PIL import Image

# Create a new image with RGB color
image = Image.new('RGB', (100, 100))

# Save the image with compression level set to 5 (0-9, 0 being no compression)
image.save("./tmp/compression_level_5.png", compress_level=5)