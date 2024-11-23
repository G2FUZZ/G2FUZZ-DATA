from PIL import Image, ImageDraw

# Create a new image with white background
width, height = 200, 200
image = Image.new('RGB', (width, height), "white")
draw = ImageDraw.Draw(image)

# Draw some shapes to demonstrate device independence
# Drawing a red rectangle
draw.rectangle([50, 50, 150, 150], outline="red", fill=None)
# Drawing a blue circle (ellipse in a square to make it look like a circle)
draw.ellipse([75, 75, 125, 125], outline="blue", fill=None)
# Drawing a green line
draw.line([0, 0, width, height], fill="green", width=5)

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Save the image as a BMP file
image.save('./tmp/demo_device_independence.bmp')

print("BMP file has been saved to ./tmp/demo_device_independence.bmp")