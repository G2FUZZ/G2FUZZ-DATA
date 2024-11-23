from PIL import Image

# Create an RGBA image with Progressive Loading and multiple layers
rgba_image = Image.new('RGBA', (200, 200), color='green')
rgba_image.save('./tmp/rgba_image.tif', tiffinfo={274: 2, 277: 4})

# Create an RGB image with LZW compression
rgb_image_lzw = Image.new('RGB', (200, 200), color='blue')
rgb_image_lzw.save('./tmp/rgb_image_lzw.tif', compression='tiff_lzw')

# Create a CMYK image with PackBits compression
cmyk_image_packbits = Image.new('CMYK', (200, 200), color='magenta')
cmyk_image_packbits.save('./tmp/cmyk_image_packbits.tif', compression='packbits')