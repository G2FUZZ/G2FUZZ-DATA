from PIL import Image

# Create a new image with RGB mode
img = Image.new('RGB', (100, 100))

# Progressive encoding
img.save('./tmp/progressive_encoded.jpg', 'JPEG', quality=95, optimize=True, progressive=True)