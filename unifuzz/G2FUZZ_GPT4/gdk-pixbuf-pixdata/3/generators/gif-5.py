from PIL import Image, ImageDraw
import os

# Ensure the tmp directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a new image with white background
width, height = 200, 200
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Draw a simple house
draw.polygon([(100, 50), (50, 100), (150, 100)], outline="red", fill="blue")
draw.rectangle((50, 100, 150, 150), outline="red", fill="green")

# Save the image as interlaced GIF
image.save(output_dir + "interlaced_house.gif", "GIF", interlace=True)