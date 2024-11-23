from PIL import Image, ImageDraw, ImageFont

# Create a new image with white background
width, height = 400, 400
image = Image.new('RGB', (width, height), "white")
draw = ImageDraw.Draw(image)

# Drawing a red rectangle with rounded corners
draw.rounded_rectangle([10, 10, 190, 190], fill="red", outline="black", width=3, radius=20)

# Drawing a blue circle
draw.ellipse([210, 10, 390, 190], outline="blue", fill="skyblue", width=5)

# Drawing a green polygon (triangle)
draw.polygon([(100, 300), (300, 300), (200, 100)], fill="green", outline="yellow")

# Create a gradient-filled rectangle
for i in range(100):
    color = 255 - int((i / 100) * 255)
    draw.line([(200, 200 + i), (300, 200 + i)], fill=(255, color, 0), width=1)

# Drawing a green line with width of 5
draw.line([0, 0, width, height], fill="green", width=5)

# Adding text to the image
try:
    # Attempt to use a TTF font
    font = ImageFont.truetype("arial.ttf", 24)
except IOError:
    # Falling back to the default PIL font if TTF font is not found
    font = ImageFont.load_default()

draw.text((10, 350), "Hello World!", fill="purple", font=font)

# Draw multiple lines to form a grid
for x in range(0, width, 20):
    draw.line([(x, 0), (x, height)], fill="lightgray")
for y in range(0, height, 20):
    draw.line([(0, y), (width, y)], fill="lightgray")

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Save the image as a BMP file
image.save('./tmp/complex_demo_device_independence.bmp')

print("BMP file has been saved to ./tmp/complex_demo_device_independence.bmp")