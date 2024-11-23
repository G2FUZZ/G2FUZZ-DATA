from PIL import Image, ImageDraw

# Create an image with RGB mode
width, height = 800, 600
image = Image.new('RGB', (width, height), "black")
draw = ImageDraw.Draw(image)

# Generate a vertical gradient
for i in range(height):
    r = int(i / height * 255)
    g = 255 - int(i / height * 255)
    b = 128 # Constant value for simplicity
    draw.line((0, i, width, i), fill=(r,g,b))

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image with progressive loading feature
image.save('./tmp/progressive_loading.jpg', 'JPEG', quality=80, progressive=True)