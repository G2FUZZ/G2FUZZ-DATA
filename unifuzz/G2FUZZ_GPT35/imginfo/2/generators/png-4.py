from PIL import Image

# Create an 8-bit grayscale image
image_gray = Image.new('L', (100, 100))
image_gray.save('./tmp/8bit_grayscale.png')

# Create a 24-bit RGB image
image_rgb = Image.new('RGB', (100, 100), color='red')
image_rgb.save('./tmp/24bit_rgb.png')

# Create a 48-bit RGB with alpha channel image
image_rgba = Image.new('RGBA', (100, 100), color='green')
image_rgba.save('./tmp/48bit_rgba.png')