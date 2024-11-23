from PIL import Image

# Create a white image
white_image = Image.new('RGB', (100, 100), 'white')
white_image.save('./tmp/lossy_compression.jpg', quality=90)