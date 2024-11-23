from PIL import Image, ImageDraw

# Define image size and channels
width, height = 200, 200

# Create a new image with an alpha channel (transparency)
image = Image.new("RGBA", (width, height), (255, 255, 255, 0))

# Initialize the drawing context
draw = ImageDraw.Draw(image)

# Define circle parameters
circle_center = (width // 2, height // 2)
circle_radius = 60
circle_color = (255, 0, 0, 255)  # Red with full opacity

# Draw a circle
draw.ellipse([circle_center[0] - circle_radius, circle_center[1] - circle_radius,
              circle_center[0] + circle_radius, circle_center[1] + circle_radius], fill=circle_color)

# Ensure the './tmp/' directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image
file_path = './tmp/transparent_circle.bmp'
image.save(file_path)

print(f"Image saved to {file_path}")