from PIL import Image

# Create an RGB image with resolution information (300 DPI)
rgb_image = Image.new('RGB', (100, 100), color='red')
rgb_image.save('./tmp/rgb_image_with_resolution.tif', dpi=(300, 300))

# Create a CMYK image with resolution information (200 DPI)
cmyk_image = Image.new('CMYK', (100, 100), color='cyan')
cmyk_image.save('./tmp/cmyk_image_with_resolution.tif', dpi=(200, 200))

# Create a grayscale image with resolution information (150 DPI)
grayscale_image = Image.new('L', (100, 100), color='gray')
grayscale_image.save('./tmp/grayscale_image_with_resolution.tif', dpi=(150, 150))