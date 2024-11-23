from PIL import Image, ImageDraw, ImageFont

# Text to be added
text = """8. Compatibility: BMP files are widely supported across various operating systems and software applications, making them a versatile choice for storing and sharing images, despite their larger size."""

# Image size
width, height = 800, 200

# Creating a new image with white background
image = Image.new('RGB', (width, height), color = (255, 255, 255))

# Initializing the drawing context
draw = ImageDraw.Draw(image)

# Font settings (using default PIL font)
font_size = 14
font = ImageFont.load_default()

# Position for the text to start
x, y = 10, 10

# Adding text to image
draw.text((x, y), text, fill=(0, 0, 0), font=font)

# Creating the ./tmp/ directory if it doesn't exist
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Saving the image in BMP format
file_path = './tmp/compatibility.bmp'
image.save(file_path, 'BMP')

print(f"Image saved at {file_path}")