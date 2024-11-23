from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with RGB mode and white background
width, height = 100, 100
image = Image.new('RGB', (width, height), "white")

# Optionally, you can draw on the image to add some features
# For simplicity, let's draw a simple red square
draw = ImageDraw.Draw(image)
draw.rectangle([25, 25, 75, 75], fill ="red")

# Save the image as a PNG file
image.save('./tmp/test.png', format='PNG')

print("PNG file has been created at ./tmp/test.png")