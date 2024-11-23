import os
from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new blank image using RGBA mode for transparency
size = (256, 256)  # Common icon size
image = Image.new('RGBA', size, color=(255, 255, 255, 0))

# Draw on the image to make it unique. Let's draw a simple shape.
draw = ImageDraw.Draw(image)
draw.rectangle([size[0]//4, size[1]//4, 3*size[0]//4, 3*size[1]//4], fill="red", outline="blue")

# Save the image as an ICO file
# The ICO format supports saving multiple sizes. Here we just save the one size.
ico_path = './tmp/sample_icon.ico'
image.save(ico_path, format='ICO', sizes=[size])

print(f"ICO file saved at {ico_path}")