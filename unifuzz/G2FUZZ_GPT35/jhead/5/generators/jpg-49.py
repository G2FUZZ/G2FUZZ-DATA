import numpy as np
from PIL import Image, ImageDraw, ImageFont
import matplotlib.font_manager as fm

# Create a white image of size 400x400 pixels
image = np.ones((400, 400, 3), dtype=np.uint8) * 255
image = Image.fromarray(image)

# Add shapes and gradients to the image
draw = ImageDraw.Draw(image)

# Draw a rectangle with a gradient fill
draw.rectangle([(50, 50), (150, 150)], fill=(255, 0, 0), outline=None)
for i in range(51):
    draw.rectangle([(50+i, 50+i), (150-i, 150-i)], fill=(255-i*2, 0, 0), outline=None)

# Add text with different styles to the image
font_paths = fm.findSystemFonts()
font_bold = ImageFont.truetype(font_paths[0], 24)  # Use the first font found
font_italic = ImageFont.truetype(font_paths[1], 32)  # Use the second font found

draw.text((50, 200), "Complex Features!", fill=(0, 0, 0), font=font_bold)
draw.text((50, 250), "Lorem ipsum dolor sit amet", fill=(0, 0, 0), font=font_italic)

# Save the image as a jpg file
image.save("./tmp/complex_features.jpg")

print("Complex features jpg file generated successfully!")