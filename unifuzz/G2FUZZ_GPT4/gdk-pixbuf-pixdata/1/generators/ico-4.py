from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Create a new blank (transparent) image
size = (256, 256)  # Icon size
image = Image.new("RGBA", size, (255, 0, 0, 0))  # RGBA for transparency

# Draw a red circle on the transparent image
draw = ImageDraw.Draw(image)
circle_radius = 100
circle_position = (size[0]//2, size[1]//2)
draw.ellipse((circle_position[0]-circle_radius, circle_position[1]-circle_radius, circle_position[0]+circle_radius, circle_position[1]+circle_radius), fill=(255, 0, 0, 255))

# Save the image as an ICO file with multiple sizes for compatibility
icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
image.save('./tmp/icon_with_transparency.ico', format='ICO', sizes=icon_sizes)