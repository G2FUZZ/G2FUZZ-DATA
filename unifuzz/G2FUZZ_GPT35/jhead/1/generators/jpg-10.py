from PIL import Image

# Create a white image
white_image = Image.new('RGB', (100, 100), (255, 255, 255))
white_image.save('./tmp/white.jpg')

# Create a black image
black_image = Image.new('RGB', (100, 100), (0, 0, 0))
black_image.save('./tmp/black.jpg')