from PIL import Image

# Create an RGB image
image_rgb = Image.new('RGB', (100, 100), color='red')
image_rgb.save('./tmp/rgb_image.png')

# Create a grayscale image
image_gray = Image.new('L', (100, 100), color='gray')
image_gray.save('./tmp/gray_image.png')

# Create an indexed color image
image_indexed = Image.new('P', (100, 100))
image_indexed.putpalette([0, 0, 0, 255, 255, 255])  # Black and White palette
image_indexed.putpixel((50, 50), 1)  # Set a white pixel
image_indexed.save('./tmp/indexed_image.png')