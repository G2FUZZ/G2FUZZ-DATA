import io
from PIL import Image

# Create images with different color depths
image_mono = Image.new('1', (32, 32))  # monochrome image
image_16_colors = Image.new('P', (32, 32))  # 16 colors image
image_256_colors = Image.new('P', (32, 32))  # 256 colors image
image_true_color = Image.new('RGB', (32, 32))  # true color image

# Save the images as ICO files
image_mono.save('./tmp/mono.ico')
image_16_colors.save('./tmp/16_colors.ico')
image_256_colors.save('./tmp/256_colors.ico')
image_true_color.save('./tmp/true_color.ico')