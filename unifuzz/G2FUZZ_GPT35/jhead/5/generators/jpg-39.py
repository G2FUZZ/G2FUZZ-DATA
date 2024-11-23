from PIL import Image, ImageDraw, ImageFilter, ImageFont
import os

# Create a sample image with gradient background
gradient = Image.new('RGB', (300, 200))
for x in range(gradient.width):
    for y in range(gradient.height):
        gradient.putpixel((x, y), (x, y, 255))
gradient.save('./tmp/gradient.jpg')

# Apply a blur filter on the image
gradient_blurred = gradient.filter(ImageFilter.GaussianBlur(5))
gradient_blurred.save('./tmp/gradient_blurred.jpg')

# Add text overlay to the blurred image
draw = ImageDraw.Draw(gradient_blurred)
font = ImageFont.load_default()
draw.text((10, 10), "Blurred Image", fill='white', font=font)
gradient_blurred.save('./tmp/gradient_blurred_text.jpg')