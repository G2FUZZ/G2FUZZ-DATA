from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Image dimensions and background color
width, height = 400, 400
background_color = (0, 100, 200, 255)  # Solid color background with no transparency

# Create a new RGBA image
image = Image.new('RGBA', (width, height), color=background_color)

# Draw a semi-transparent circle in the middle
draw = ImageDraw.Draw(image)
circle_center = width // 2, height // 2
circle_radius = 100
circle_color = (255, 0, 0, 128)  # Semi-transparent red
draw.ellipse([circle_center[0]-circle_radius, circle_center[1]-circle_radius,
              circle_center[0]+circle_radius, circle_center[1]+circle_radius], fill=circle_color)

# Save the image as a TGA file
tga_path = os.path.join(output_dir, 'image_with_alpha.tga')
image.save(tga_path, format='TGA')

print(f"Image saved to {tga_path}")