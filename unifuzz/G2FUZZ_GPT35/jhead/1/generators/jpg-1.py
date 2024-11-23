from PIL import Image

# Create a new image with RGB mode
img = Image.new('RGB', (100, 100), color = 'red')
img.save('./tmp/lossy_compression.jpg')