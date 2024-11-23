from PIL import Image
import os

# Create a directory to save the file if it doesn't exist
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the image size and background color
width, height = 100, 100  # Example dimensions
background_color = (255, 0, 0)  # Example color (red) in RGB

# Create a new image with RGB mode
image = Image.new('RGB', (width, height), color=background_color)

# Example: Modify pixels here if needed
# This is where you can control image composition at the pixel level
# For demonstration, let's draw a simple pattern
for x in range(0, width, 10):
    for y in range(0, height, 10):
        image.putpixel((x, y), (0, 255, 0))  # Change color at these pixels to green

# Save the image in a supported format, such as PNG
output_path = os.path.join(output_dir, 'example.png')
image.save(output_path, 'PNG')

print(f'Image saved as {output_path}')