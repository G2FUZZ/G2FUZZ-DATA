from PIL import Image, ImageDraw, ImageFont

# Text to be added to the image
text = """
10. **Wide Compatibility**: BMP files are widely supported across operating systems,
software applications, and devices, making them a versatile choice for internal and archival
purposes, despite their large sizes compared to more modern image formats.
"""

# Create an image with white background
width, height = 800, 600
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Define the font and size
# Note: You can specify a different font or path to a .ttf file with ImageFont.truetype()
font = ImageFont.load_default()

# Calculate text width and height
textwidth, textheight = draw.textsize(text, font)

# Calculate the x,y coordinates of the text
x = (width - textwidth) / 2
y = (height - textheight) / 2

# Add text to image
draw.text((x, y), text, fill="black", font=font)

# Ensure the './tmp/' directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image
image.save('./tmp/wide_compatibility.bmp')

print("BMP file has been saved to ./tmp/wide_compatibility.bmp")