from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image with PIL
image_size = (800, 600)
image = Image.new('RGB', image_size, color = 'blue')
draw = ImageDraw.Draw(image)
draw.text((10, 10), 'Hello, World!', fill=(255, 255, 255))

# Adjustable Compression Levels
# Quality ranges from 1 (worst) to 95 (best). The default is 75.
# Values above 95 should be avoided; 100 disables portions of the JPEG compression algorithm.
compression_levels = [10, 50, 75, 95]

for level in compression_levels:
    filename = f'./tmp/sample_{level}.jpg'
    image.save(filename, 'JPEG', quality=level)