from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Create an image with transparent background
width, height = 400, 400
image = Image.new("RGBA", (width, height), (255, 0, 0, 0))

# Initialize the drawing context
draw = ImageDraw.Draw(image)

# Draw a semi-transparent red circle in the center
circle_radius = 100
circle_center = (width // 2, height // 2)
draw.ellipse([circle_center[0] - circle_radius, circle_center[1] - circle_radius,
              circle_center[0] + circle_radius, circle_center[1] + circle_radius], 
             fill=(255, 0, 0, 128))  # Semi-transparent red

# Save the image with transparency
image.save('./tmp/transparent_circle.png')