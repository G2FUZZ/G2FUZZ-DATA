import os
from PIL import Image, ImageDraw, ImageFont

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the size of the image (width, height)
size = (400, 400)

# Create the layers
# Layer 1: Background
background = Image.new('RGBA', size, (255, 200, 150, 255))  # Orange background

# Layer 2: Adding some text
text_layer = Image.new('RGBA', size, (255, 255, 255, 0))  # Transparent layer
draw = ImageDraw.Draw(text_layer)

# Use a default font provided by PIL/Pillow
font = ImageFont.load_default()

# If you specifically need to use Arial or another font, you would need to provide its path directly, as mentioned earlier.
# For example: font = ImageFont.truetype("/path/to/fonts/arial.ttf", size=40)

draw.text((50, 150), "Hello", fill=(0, 0, 0, 255), font=font)

# Layer 3: A simple drawing
drawing_layer = Image.new('RGBA', size, (255, 255, 255, 0))  # Transparent layer
draw = ImageDraw.Draw(drawing_layer)
draw.rectangle([100, 250, 300, 350], fill=(70, 130, 180, 180))  # Semi-transparent blue rectangle

# Merge the layers
final_image = Image.alpha_composite(background, text_layer)
final_image = Image.alpha_composite(final_image, drawing_layer)

# Save the final image
final_image.save('./tmp/final_image.png')