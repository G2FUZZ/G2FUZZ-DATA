from PIL import Image

# Create a new image with 24-bit true color support
image = Image.new('RGB', (100, 100), color='white')
image.save('./tmp/true_color_image.png')