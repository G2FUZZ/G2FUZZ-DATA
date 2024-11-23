from PIL import Image

# Create a RGB image
image_rgb = Image.new('RGB', (100, 100), color='red')
image_rgb.save('./tmp/rgb_image.jpg')

# Create a CMYK image
image_cmyk = Image.new('CMYK', (100, 100), color='cyan')
image_cmyk.save('./tmp/cmyk_image.jpg')

# Create a Grayscale image
image_gray = Image.new('L', (100, 100), color='gray')
image_gray.save('./tmp/grayscale_image.jpg')