import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs("./tmp/", exist_ok=True)

# Create a simple image in JPEG format
img_jpeg = Image.new('RGB', (64, 64), color='blue')
jpeg_path = './tmp/sample_jpeg.jpg'
img_jpeg.save(jpeg_path)

# Create a simple image in GIF format
img_gif = Image.new('RGB', (32, 32), color='green')
gif_path = './tmp/sample_gif.gif'
img_gif.save(gif_path)

# Now, we'll convert these images to ICO format, including them in a single ICO file

ico_path = './tmp/multi_format_images.ico'

# Open the images
img_jpeg = Image.open(jpeg_path)
img_gif = Image.open(gif_path)

# Since we cannot directly save multiple distinct images in an ICO file using PIL,
# we will demonstrate saving a single image (JPEG) as an ICO.
# For a real application, consider creating multiple sizes of the same image for the ICO,
# or use a specialized library or tool that supports creating ICO files with distinct images.

# Save the JPEG image as an ICO file
img_jpeg.save(ico_path, format='ICO', sizes=[(64, 64)])

print("ICO file saved.")