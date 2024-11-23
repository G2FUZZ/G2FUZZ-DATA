from PIL import Image

# Create RGB image
rgb_img = Image.new('RGB', (100, 100), color='green')
rgb_img.save('./tmp/rgb_image.jpg')

# Create CMYK image
cmyk_img = Image.new('CMYK', (100, 100), color='cyan')
cmyk_img.save('./tmp/cmyk_image.jpg')

# Create grayscale image
gray_img = Image.new('L', (100, 100), color='gray')
gray_img.save('./tmp/grayscale_image.jpg')