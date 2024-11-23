from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Create a new PNG image with RGBA (Red, Green, Blue, Alpha) color space
size = (256, 256)  # Size of the icon
image = Image.new('RGBA', size, (255, 255, 255, 0))  # Transparent background

# Draw a simple shape with semi-transparency
draw = ImageDraw.Draw(image)
draw.ellipse((64, 64, 192, 192), fill=(255, 0, 0, 128))  # Semi-transparent red circle

# Save the image as a PNG file temporarily
temp_file_path = './tmp/temp_icon.png'
image.save(temp_file_path, format='PNG')

# Now, convert the PNG image to ICO format
icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]  # Common ICO sizes
image.save('./tmp/generated_icon.ico', format='ICO', sizes=icon_sizes)

# Optionally, clean up the temporary PNG file
os.remove(temp_file_path)

print("ICO file has been generated and saved to ./tmp/generated_icon.ico")