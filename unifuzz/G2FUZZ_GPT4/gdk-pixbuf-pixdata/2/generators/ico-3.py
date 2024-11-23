from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Create a transparent PNG image
img_size = (256, 256)
image = Image.new("RGBA", img_size, (255, 255, 255, 0))

# Draw a simple shape on the image
draw = ImageDraw.Draw(image)
draw.ellipse((56, 56, 200, 200), fill=(255, 0, 0, 255), outline=(0, 0, 0))

# Save the image as a PNG file (for demonstration purposes, not strictly needed for the ICO)
image.save('./tmp/test.png', format='PNG')

# Now, save the PNG image as an ICO file
icon_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
image.save('./tmp/test.ico', format='ICO', sizes=icon_sizes)