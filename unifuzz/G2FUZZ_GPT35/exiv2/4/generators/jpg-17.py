from PIL import Image

# Create a new image with RGB mode
img = Image.new('RGB', (100, 100))

# Progressive encoding with DCT compression
img.save('./tmp/progressive_encoded_with_dct_and_thumbnail.jpg', 'JPEG', quality=95, optimize=True, progressive=True, dct_mode='1', thumbnail=img.resize((64, 64)))