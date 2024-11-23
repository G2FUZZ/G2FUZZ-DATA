from PIL import Image

# Create a new JPG image with compression artifacts
img = Image.new('RGB', (100, 100), color='white')
img.save('./tmp/compression_artifacts.jpg', quality=10)