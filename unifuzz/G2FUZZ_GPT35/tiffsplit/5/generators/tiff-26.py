from PIL import Image

# Create an RGB image with compression quality settings
rgb_image = Image.new('RGB', (100, 100), color='red')
rgb_image.save('./tmp/rgb_image_with_compression.tif', compression='tiff_lzw')

# Create a CMYK image with compression quality settings
cmyk_image = Image.new('CMYK', (100, 100), color='cyan')
cmyk_image.save('./tmp/cmyk_image_with_compression.tif', compression='tiff_deflate')

# Create a grayscale image with compression quality settings
grayscale_image = Image.new('L', (100, 100), color='gray')
grayscale_image.save('./tmp/grayscale_image_with_compression.tif', compression='tiff_adobe_deflate')