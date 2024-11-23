from PIL import Image

# Create an RGB image with a red square
image_rgb = Image.new('RGB', (100, 100), color='white')
image_rgb.paste((255, 0, 0), (25, 25, 75, 75))
image_rgb.save('./tmp/rgb_image.jpg')

# Create a CMYK image with a blue square
image_cmyk = Image.new('CMYK', (100, 100), color='white')
image_cmyk.paste((255, 0, 0, 0), (25, 25, 75, 75))
image_cmyk.save('./tmp/cmyk_image.jpg')