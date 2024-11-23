from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)  # Corrected argument name here

# Create a new image with a white background
width, height = 800, 600
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Draw some patterns to illustrate different data types in images
# Horizontal lines
for i in range(0, height, 10):
    draw.line([(0, i), (width, i)], fill='black')

# Vertical lines
for i in range(0, width, 10):
    draw.line([(i, 0), (i, height)], fill='black')

# Diagonal lines
for i in range(0, width, 20):
    draw.line([(i, 0), (0, i)], fill='red')
for i in range(0, height, 20):
    draw.line([(0, i), (width, height-i)], fill='red')

# Save the image
image_path = './tmp/filter_methods_demo.png'
image.save(image_path, 'PNG')

print(f"Image saved at {image_path}")