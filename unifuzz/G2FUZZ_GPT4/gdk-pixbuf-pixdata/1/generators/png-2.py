from PIL import Image, ImageDraw

# Create an image with transparent background
width, height = 200, 200
image = Image.new('RGBA', (width, height), (255, 0, 0, 0))

# Draw a red circle with a defined opacity in the center of the image
draw = ImageDraw.Draw(image)
circle_radius = 60
circle_opacity = 255  # Fully opaque (0 for fully transparent)
circle_color = (255, 0, 0, circle_opacity)  # Red with defined opacity
draw.ellipse((width/2 - circle_radius, height/2 - circle_radius, width/2 + circle_radius, height/2 + circle_radius), fill=circle_color)

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image with transparency
image.save('./tmp/transparent_image.png')