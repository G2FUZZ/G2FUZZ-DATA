from PIL import Image

# Create an RGB image with Image Pyramids
rgb_image = Image.new('RGB', (100, 100), color='red')
rgb_image.save('./tmp/rgb_image_with_pyramids.tif', "TIFF", tiffinfo=rgb_image.info)

# Create a CMYK image with Image Pyramids
cmyk_image = Image.new('CMYK', (100, 100), color='cyan')
cmyk_image.save('./tmp/cmyk_image_with_pyramids.tif', "TIFF", tiffinfo=cmyk_image.info)

# Create a grayscale image with Image Pyramids
grayscale_image = Image.new('L', (100, 100), color='gray')
grayscale_image.save('./tmp/grayscale_image_with_pyramids.tif', "TIFF", tiffinfo=grayscale_image.info)