from PIL import Image

# Create a new image with RGB mode
image = Image.new('RGB', (100, 100))

# Save the image in jpg format with a compression quality of 80
image.save('./tmp/compression_ratio.jpg', quality=80)