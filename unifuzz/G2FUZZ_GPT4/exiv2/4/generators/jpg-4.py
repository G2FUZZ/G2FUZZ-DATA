from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate a simple image with PIL
img = Image.new('RGB', (100, 100), color = (73, 109, 137))

# Draw a rectangle for visualization
d = ImageDraw.Draw(img)
d.rectangle([10, 10, 90, 90], fill=(255, 255, 0))

# Save the image in progressive JPEG format
progressive_jpeg_path = os.path.join(output_dir, "progressive_image.jpg")
img.save(progressive_jpeg_path, "JPEG", quality=80, progressive=True)