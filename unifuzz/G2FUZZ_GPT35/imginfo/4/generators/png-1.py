from PIL import Image

# Create a white image
white_image = Image.new('RGB', (100, 100), (255, 255, 255))
white_image.save('./tmp/lossless_compression.png', 'PNG')