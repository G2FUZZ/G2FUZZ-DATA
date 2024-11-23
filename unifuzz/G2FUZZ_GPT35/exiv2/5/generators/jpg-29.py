from PIL import Image

# Create an RGB image
rgb_image = Image.new('RGB', (100, 100), color='red')
rgb_image.save('./tmp/rgb_image.jpg', format='JPEG', subsampling=0, quality=95, thumbnail=Image.new('RGB', (32, 32), color='red'))

# Create a CMYK image
cmyk_image = Image.new('CMYK', (100, 100), color='cyan')
cmyk_image.save('./tmp/cmyk_image.jpg', format='JPEG', subsampling=0, quality=95, thumbnail=Image.new('CMYK', (32, 32), color='cyan'))

# Create a grayscale image
grayscale_image = Image.new('L', (100, 100), color='gray')
grayscale_image.save('./tmp/grayscale_image.jpg', format='JPEG', subsampling=0, quality=95, thumbnail=Image.new('L', (32, 32), color='gray'))

# Convert existing JPEG files to Progressive WebP format
from PIL import WebPImagePlugin
WebPImagePlugin.WebPImagePlugin_save_handler = WebPImagePlugin.WebPImageFile

rgb_image.save('./tmp/rgb_image.webp', format='WEBP', quality=95, method=6, lossless=False)
cmyk_image.save('./tmp/cmyk_image.webp', format='WEBP', quality=95, method=6, lossless=False)
grayscale_image.save('./tmp/grayscale_image.webp', format='WEBP', quality=95, method=6, lossless=False)