from PIL import Image, ImageDraw

# Create an image with a single layer
width, height = 400, 400
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Draw a simple representation of single-layer limitation
# Draw a background
draw.rectangle([0, 0, width, height], fill="skyblue")

# Draw some elements on the "single layer"
draw.rectangle([100, 100, 300, 300], fill="lightgreen", outline="black", width=2)
draw.ellipse([120, 120, 280, 280], fill="salmon", outline="black", width=2)
draw.line([100, 100, 300, 300], fill="black", width=2)
draw.line([100, 300, 300, 100], fill="black", width=2)
draw.text((150, 190), "No Layers", fill="black")

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Save the image
file_path = './tmp/no_layers.bmp'
image.save(file_path)

print(f"Image saved to {file_path}")