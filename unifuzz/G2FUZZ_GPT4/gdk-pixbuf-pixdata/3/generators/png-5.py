import os
from PIL import Image, ImageDraw

# Ensure the target directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Create a new image with a white background
width, height = 800, 600
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Draw some shapes to demonstrate interlacing
draw.ellipse((200, 150, 600, 450), outline="blue", width=5)
draw.rectangle((300, 200, 500, 400), outline="green", width=5)
draw.line((0, 0, width, height), fill="red", width=3)
draw.line((0, height, width, 0), fill="red", width=3)

# Save the image with interlacing enabled (PNG format supports it)
image.save(os.path.join(output_dir, "interlaced_image.png"), "PNG", interlace=1)

print("Interlaced PNG image has been saved.")