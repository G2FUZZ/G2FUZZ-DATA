from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a new image with a white background
img_size = (200, 200)
image = Image.new('RGB', img_size, 'white')
draw = ImageDraw.Draw(image)

# Draw some simple shapes to visualize the interlacing effect
draw.line((0, 0) + img_size, fill=128)
draw.line((0, img_size[1], img_size[0], 0), fill=128)
draw.ellipse((50, 50, 150, 150), outline="black")

# Save the image with interlacing enabled (PNG format supports interlacing)
output_path = os.path.join(output_dir, 'interlaced_image.png')
# When saving a PNG, the 'optimize' flag must be False to save with interlacing
image.save(output_path, 'PNG', interlace=1)

print(f"Image saved to {output_path}")