from PIL import Image, ImageDraw
import os
from random import randint  # Import randint

# Create an RGBA image (Red, Green, Blue, Alpha)
width, height = 400, 400
image = Image.new("RGBA", (width, height))

# Draw a gradient background
for y in range(height):
    for x in range(width):
        # Gradient from blue to green
        R = 0
        G = y % 256  # Cycle green from 0 to 255
        B = (255 - y) % 256  # Cycle blue from 255 to 0
        image.putpixel((x, y), (R, G, B, 255))

# Initialize ImageDraw
draw = ImageDraw.Draw(image)

# Draw semi-transparent circles
for i in range(10, 100, 20):  # Start, stop, step for the circles' radii
    for j in range(5):  # Number of circles for each radius
        # Randomly place circles, ensuring they're partially within bounds
        x, y = randint(50, 350), randint(50, 350)
        # Semi-transparent circles with random colors
        R = randint(100, 255)
        G = randint(100, 255)
        B = randint(100, 255)
        draw.ellipse((x-i, y-i, x+i, y+i), fill=(R, G, B, 128))

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image as TGA
image.save('./tmp/complex_example_with_alpha.tga')