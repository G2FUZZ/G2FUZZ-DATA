from PIL import Image, ImageDraw, ImageFont
import random

# Create a new JPG file with RGB color space
img = Image.new('RGB', (600, 400), color=(255, 255, 255))

# Initialize the drawing context
d = ImageDraw.Draw(img)

# Load a font
font = ImageFont.load_default()

# Add text to the image
d.text((20, 20), "Complex File Structures Example", fill=(0, 0, 0), font=font)

# Draw shapes on the image
d.rectangle([(50, 50), (200, 200)], fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
d.ellipse([(250, 50), (400, 200)], fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

# Create a gradient effect
for x in range(600):
    for y in range(200, 400):
        img.putpixel((x, y), (x % 256, (x + y) % 256, y % 256))

# Save the image
img.save('./tmp/complex_file_structure_example.jpg')