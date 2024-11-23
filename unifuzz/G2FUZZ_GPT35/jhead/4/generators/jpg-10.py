from PIL import Image

# Create a white image
white_image = Image.new('RGB', (100, 100), 'white')
white_image.save('./tmp/white_image.jpg')

# Create a black image
black_image = Image.new('RGB', (100, 100), 'black')
black_image.save('./tmp/black_image.jpg')

# Create a red image
red_image = Image.new('RGB', (100, 100), 'red')
red_image.save('./tmp/red_image.jpg')

# Create a green image
green_image = Image.new('RGB', (100, 100), 'green')
green_image.save('./tmp/green_image.jpg')

# Create a blue image
blue_image = Image.new('RGB', (100, 100), 'blue')
blue_image.save('./tmp/blue_image.jpg')

print('JPG files with different features have been generated and saved in ./tmp/')