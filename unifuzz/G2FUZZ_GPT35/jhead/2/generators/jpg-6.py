from PIL import Image

# Create a sample image
image = Image.new('RGB', (100, 100), color='red')
image.save('./tmp/image_compression_level_10.jpg', quality=10)
image.save('./tmp/image_compression_level_50.jpg', quality=50)
image.save('./tmp/image_compression_level_80.jpg', quality=80)
image.save('./tmp/image_compression_level_100.jpg', quality=100)