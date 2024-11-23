from PIL import Image, ImageDraw, ImageFont
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a more complex image with a larger size and more elements
width, height = 200, 200
image = Image.new('RGB', (width, height), 'skyblue')
draw = ImageDraw.Draw(image)

# Drawing a rectangle with rounded corners
draw.rounded_rectangle([10, 10, 190, 190], fill="lightblue", outline="black", width=3, radius=15)

# Drawing a circle
draw.ellipse([50, 50, 150, 150], outline="blue", fill="blue", width=5)

# Drawing a polygon (triangle)
draw.polygon([(50, 180), (150, 180), (100, 60)], fill="green", outline="yellow")

# Adding gradient
for i in range(100):
    color = 255 - int((i / 100) * 255)
    draw.line([(50, 50 + i), (150, 50 + i)], fill=(255, color, 0), width=1)

# Adding text to the image
try:
    # Attempt to use a TTF font
    font = ImageFont.truetype("arial.ttf", 18)
except IOError:
    # Falling back to the default PIL font if TTF font is not found
    font = ImageFont.load_default()

draw.text((10, 170), "Demo Text", fill="purple", font=font)

# Draw multiple lines to form a grid
for x in range(0, width, 20):
    draw.line([(x, 0), (x, height)], fill="lightgray")
for y in range(0, height, 20):
    draw.line([(0, y), (width, y)], fill="lightgray")

# Save the image as BMP
image_path = './tmp/complex_simple_image.bmp'
image.save(image_path)

print(f"Image saved at {image_path}")