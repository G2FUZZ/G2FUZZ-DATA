from PIL import Image

# Create a 100x100 white image
img = Image.new('RGB', (100, 100), color='white')
img.save('./tmp/lossy_compression.jpg')