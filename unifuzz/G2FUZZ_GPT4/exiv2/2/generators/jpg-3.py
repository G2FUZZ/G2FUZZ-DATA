from PIL import Image, ImageDraw

# Ensure you have Pillow installed: pip install Pillow

# Create a new image with RGB mode
width, height = 800, 600
image = Image.new('RGB', (width, height))

# Create a gradient
draw = ImageDraw.Draw(image)
for i in range(width):
    gradient_color = int(255 * (i/width))
    draw.line((i, 0, i, height), fill=(gradient_color, gradient_color, gradient_color))

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image as a progressive JPEG
image.save('./tmp/progressive_image.jpg', 'JPEG', quality=95, progressive=True)