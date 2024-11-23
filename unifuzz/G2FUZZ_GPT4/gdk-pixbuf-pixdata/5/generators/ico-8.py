import os
from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Create a new image with RGBA (Red, Green, Blue, Alpha) color space, 256x256 pixels
icon_size = (256, 256)
image = Image.new("RGBA", icon_size, color=(255, 255, 255, 0))

# Draw a simple shape - here, we're drawing a red circle
draw = ImageDraw.Draw(image)
draw.ellipse([(64, 64), (192, 192)], fill=(255, 0, 0, 255))

# Specify the path to save the ICO file
ico_path = os.path.join(output_dir, 'example_icon.ico')

# Save the image as an ICO file
image.save(ico_path, format='ICO', sizes=[icon_size])

print(f"ICO file saved at: {ico_path}")