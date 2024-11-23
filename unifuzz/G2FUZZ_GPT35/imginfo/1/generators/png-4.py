from PIL import Image

# Create a 256-color (8-bit) PNG image
img_8bit = Image.new('P', (100, 100))
img_8bit.putpalette([i for rgb in [(x, x, x) for x in range(256)] for i in rgb])
img_8bit.save('./tmp/8bit.png')

# Create a true color (24-bit) PNG image
img_24bit = Image.new('RGB', (100, 100), color='red')
img_24bit.save('./tmp/24bit.png')

# Create a true color with alpha channel (48-bit) PNG image
img_48bit = Image.new('RGBA', (100, 100), color='green')
img_48bit.save('./tmp/48bit.png')