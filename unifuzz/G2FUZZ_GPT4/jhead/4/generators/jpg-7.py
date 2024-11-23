import os
from PIL import Image, ImageDraw

# Create target directory if it doesn't exist
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define image size
width, height = 800, 600

# Create a new image with white background
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Add some graphics to the image (simple shapes here as an example)
draw.ellipse((200, 150, 600, 450), fill='lightblue', outline='blue')
draw.rectangle((100, 100, 700, 500), fill=None, outline='green')
draw.line((0, 0) + image.size, fill='red', width=10)
draw.line((0, image.size[1], image.size[0], 0), fill='red', width=10)

# Save the image with different compression levels
# Compression levels in PIL for JPEG range from 1 (worst) to 95 (best)
# Additional levels (96-100) change the subsampling to 4:4:4 without further quality improvement
compression_levels = [10, 50, 95]  # Examples of low, medium, and high quality

for level in compression_levels:
    output_filename = os.path.join(output_dir, f"example_quality_{level}.jpg")
    image.save(output_filename, 'JPEG', quality=level)

print("Images saved successfully.")