import os
from PIL import Image, ImageDraw

# Create the directory for output if it doesn't exist
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the image size and color palette
image_size = (200, 200)
palette = [
    0, 0, 0,        # Black
    255, 0, 0,      # Red
    0, 255, 0,      # Green
    0, 0, 255,      # Blue
    255, 255, 0,    # Yellow
    255, 165, 0,    # Orange
    255, 255, 255,  # White
] + [0, 0, 0] * 249  # Fill the rest of the 256-color palette (unused colors)

# Create a new image with an indexed color palette
image = Image.new("P", image_size)
image.putpalette(palette)

# Draw on the image
draw = ImageDraw.Draw(image)
draw.rectangle([10, 10, 60, 60], fill=1)  # Red square
draw.rectangle([70, 10, 120, 60], fill=2)  # Green square
draw.rectangle([130, 10, 180, 60], fill=3)  # Blue square
draw.ellipse([10, 70, 60, 120], fill=4)  # Yellow circle
draw.ellipse([70, 70, 120, 120], fill=5)  # Orange circle
draw.polygon([(130, 70), (180, 70), (155, 120)], fill=6)  # White triangle

# Save the image
image_path = os.path.join(output_dir, "palette_based_image.png")
image.save(image_path, "PNG")

print(f"Image saved to {image_path}")