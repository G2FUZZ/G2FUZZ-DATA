from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Function to create a gradient image
def create_gradient(width, height, color1, color2):
    base = Image.new('RGB', (width, height), color1)
    top = Image.new('RGB', (width, height), color2)
    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        mask_data.extend([int(255 * (y / height))] * width)
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

# Create a 24-bit truecolor gradient image
image_24bit = create_gradient(256, 256, (255, 0, 0), (0, 0, 255))
image_24bit.save('./tmp/24bit_truecolor.png')

# Create a high-quality image to represent 48-bit color depth
# Note: This will still be saved as a 24-bit PNG but is meant to demonstrate a high-quality color image
image_48bit_like = create_gradient(256, 256, (0, 255, 0), (255, 255, 0))
image_48bit_like.save('./tmp/48bit_like_truecolor.png')

# Create a grayscale image
image_grayscale = Image.new('L', (256, 256))
for x in range(256):
    for y in range(256):
        image_grayscale.putpixel((x, y), int(x/256*255))
image_grayscale.save('./tmp/grayscale.png')