from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Generate an image
image = Image.new(mode="RGB", size=(100, 100), color="blue")
draw = ImageDraw.Draw(image)
draw.rectangle([25, 25, 75, 75], fill="yellow")

# Save the image
image_path = './tmp/original_image.png'
image.save(image_path)

# Load the image
loaded_image = Image.open(image_path)

# Resave the image
resaved_image_path = './tmp/resaved_image.png'
loaded_image.save(resaved_image_path)