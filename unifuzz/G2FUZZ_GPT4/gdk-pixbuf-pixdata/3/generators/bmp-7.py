from PIL import Image
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Specifications for the image
width, height = 100, 100  # Size of the image
background_color = (255, 255, 255)  # White background
line_color = (0, 0, 0)  # Black color for lines

# Create a new image with white background
image = Image.new('RGB', (width, height), color=background_color)

# Draw some lines to demonstrate device independence
for i in range(0, width, 10):
    image.putpixel((i, i), line_color)  # Diagonal line from top-left to bottom-right
    image.putpixel((width-i-1, i), line_color)  # Diagonal line from top-right to bottom-left

# Save the image
image.save(output_dir + 'device_independence.bmp')

print("BMP image created and saved to ./tmp/device_independence.bmp")