from PIL import Image

# Create an RGB image with Progressive Loading
rgb_image_progressive = Image.new('RGB', (100, 100), color='red')
rgb_image_progressive.save('./tmp/rgb_image_progressive.tif', tiffinfo={274: 2})

# Create a CMYK image with Progressive Loading
cmyk_image_progressive = Image.new('CMYK', (100, 100), color='cyan')
cmyk_image_progressive.save('./tmp/cmyk_image_progressive.tif', tiffinfo={274: 2})

# Create a grayscale image with Progressive Loading
grayscale_image_progressive = Image.new('L', (100, 100), color='gray')
grayscale_image_progressive.save('./tmp/grayscale_image_progressive.tif', tiffinfo={274: 2})