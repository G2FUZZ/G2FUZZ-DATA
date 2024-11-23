from PIL import Image

# Create grayscale image
gray_img = Image.new('L', (100, 100))
gray_img.save('./tmp/gray_image.png')

# Create indexed color image
indexed_img = Image.new('P', (100, 100))
indexed_img.putpalette([
    0, 0, 0,  # Black
    255, 255, 255,  # White
])
indexed_img.putpixel((50, 50), 1)
indexed_img.save('./tmp/indexed_image.png')

# Create truecolor with alpha image
truecolor_alpha_img = Image.new('RGBA', (100, 100), (255, 0, 0, 128))
truecolor_alpha_img.save('./tmp/truecolor_alpha_image.png')