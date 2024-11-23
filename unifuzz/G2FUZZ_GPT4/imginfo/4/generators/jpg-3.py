from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a simple gradient image
width, height = 800, 600
image = Image.new("RGB", (width, height), "#FFFFFF")
draw = ImageDraw.Draw(image)

for i in range(width):
    gradient = int((i / width) * 255)
    draw.line([(i, 0), (i, height)], fill=(gradient, gradient, gradient))

# Save the image as a progressive JPEG
output_path = os.path.join(output_dir, "progressive_example.jpg")
image.save(output_path, "JPEG", quality=85, progressive=True)

print(f"Progressive JPEG saved to {output_path}")