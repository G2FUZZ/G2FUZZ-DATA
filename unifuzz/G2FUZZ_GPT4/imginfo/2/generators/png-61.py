import os
from PIL import Image, ImageDraw, ImageFont

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an image with RGBA (Red, Green, Blue, Alpha) mode for transparency
width, height = 600, 400
image = Image.new("RGBA", (width, height), (255, 255, 255, 0))  # Fully transparent background

# Initialize ImageDraw to draw on the image
draw = ImageDraw.Draw(image)

# Draw a semi-transparent square
draw.rectangle([(100, 100), (300, 300)], fill=(255, 0, 0, 128), outline=None)

# Draw a fully opaque circle
draw.ellipse([(350, 50), (450, 150)], fill=(0, 255, 0, 255), outline=(0, 0, 0))

# Draw a semi-transparent ellipse
draw.ellipse([(350, 200), (550, 300)], fill=(0, 0, 255, 128), outline=(255, 255, 255))

# Draw a line with opacity
draw.line((50, 350, 250, 350), fill=(255, 255, 0, 128), width=10)

# Adding text
try:
    font = ImageFont.truetype("arial.ttf", 24)  # You might need to adjust the path to the font file
except IOError:
    font = ImageFont.load_default()
draw.text((50, 50), "Hello, World!", fill=(0, 0, 0, 255), font=font)

# Adding a more complex shape, such as a polygon
draw.polygon([(400, 350), (500, 350), (450, 250)], fill=(255, 165, 0, 180), outline=(0, 0, 0))

# Save the image
image.save('./tmp/complex_transparent_example.png')