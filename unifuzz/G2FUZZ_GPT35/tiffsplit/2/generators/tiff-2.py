from PIL import Image

# Create a 1-bit monochrome TIFF image
image_1bit = Image.new('1', (100, 100))
image_1bit.save('./tmp/monochrome.tiff')

# Create an 8-bit grayscale TIFF image
image_8bit = Image.new('L', (100, 100))
image_8bit.save('./tmp/grayscale.tiff')

# Create a 24-bit RGB TIFF image
image_24bit = Image.new('RGB', (100, 100))
image_24bit.save('./tmp/rgb.tiff')