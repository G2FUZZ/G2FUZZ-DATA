from PIL import Image

# Create 1-bit color depth image
image_1bit = Image.new('1', (100, 100), color=0)
image_1bit.save('./tmp/1bit_color_depth.png')

# Create 8-bit color depth image
image_8bit = Image.new('L', (100, 100), color=128)
image_8bit.save('./tmp/8bit_color_depth.png')

# Create 24-bit color depth image
image_24bit = Image.new('RGB', (100, 100), color=(255, 0, 0))
image_24bit.save('./tmp/24bit_color_depth.png')