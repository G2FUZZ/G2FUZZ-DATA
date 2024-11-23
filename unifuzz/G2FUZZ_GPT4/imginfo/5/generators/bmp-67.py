import os
from PIL import Image, ImageDraw, ImageFont

# Create the target directory if it doesn't exist
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the width and height of the image
width, height = 400, 400

# Create a new RGB image
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Define a simple palette: 3 colors, black, red, and green
palette = [
    (0, 0, 0),  # black
    (255, 0, 0),  # red
    (0, 255, 0),  # green
]

# Use the palette to draw a pattern
for y in range(100):
    for x in range(100):
        if x < 100 // 3:
            color = palette[0]  # Use the first color from the palette (black)
        elif x < 2 * 100 // 3:
            color = palette[1]  # Use the second color from the palette (red)
        else:
            color = palette[2]  # Use the third color from the palette (green)
        draw.point((x, y), fill=color)

# Drawing additional shapes and patterns similar to the mutated example
draw.rounded_rectangle([10, 210, 190, 390], fill="red", outline="black", width=3, radius=20)
draw.ellipse([210, 210, 390, 390], outline="blue", fill="skyblue", width=5)
draw.polygon([(200, 300), (300, 300), (250, 200)], fill="green", outline="yellow")

# Adding text with font handling
try:
    font = ImageFont.truetype("arial.ttf", 24)
except IOError:
    font = ImageFont.load_default()
draw.text((10, 350), "Palette Example", fill="purple", font=font)

# Drawing a grid pattern
for x in range(0, width, 20):
    draw.line([(x, 0), (x, height)], fill="lightgray")
for y in range(0, height, 20):
    draw.line([(0, y), (width, y)], fill="lightgray")

# Save the image
image_path = os.path.join(output_dir, 'mutated_palette_example.bmp')
image.save(image_path, 'BMP')

print(f"Image saved to {image_path}")