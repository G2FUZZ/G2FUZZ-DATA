from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Create a new image with a white background
size = (256, 256)
image = Image.new('RGBA', size, color='white')

# Draw a simple shape
draw = ImageDraw.Draw(image)
draw.rectangle([size[0]//4, size[1]//4, 3*size[0]//4, 3*size[1]//4], fill='lightblue', outline='black')

# Save the image as an ICO file with compression for sizes 256x256 and higher
image.save(f'{output_dir}example_compressed.ico', format='ICO', sizes=[(256, 256)])