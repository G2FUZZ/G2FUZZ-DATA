from PIL import Image, ImageDraw

# Create an RGBA Image (Red, Green, Blue, Alpha)
size = (256, 256)  # Icon size
image = Image.new("RGBA", size, (255, 255, 255, 0))  # Transparent background

# Draw a semi-transparent circle
draw = ImageDraw.Draw(image)
circle_radius = 100
circle_opacity = 128  # 0 (fully transparent) to 255 (fully opaque)
draw.ellipse((size[0]//4, size[1]//4, 3*size[0]//4, 3*size[1]//4), fill=(255, 0, 0, circle_opacity))

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the icon
icon_sizes = [(16,16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
image.save('./tmp/icon_with_transparency.ico', format='ICO', sizes=icon_sizes)