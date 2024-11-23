from PIL import Image, ImageDraw

# Define the size of the icon
icon_size = (256, 256)

# Create a new image with RGBA mode (including alpha for transparency)
icon_image = Image.new("RGBA", icon_size, (0, 0, 0, 0))

# Initialize ImageDraw to draw on the image
draw = ImageDraw.Draw(icon_image)

# Define the circle parameters (center and radius)
circle_center = (icon_size[0] // 2, icon_size[1] // 2)
circle_radius = min(icon_size) // 4

# Draw a red circle with transparency
draw.ellipse((circle_center[0] - circle_radius, circle_center[1] - circle_radius,
              circle_center[0] + circle_radius, circle_center[1] + circle_radius),
             fill=(255, 0, 0, 255))

# Create the tmp directory if it does not exist
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the icon image
icon_image.save('./tmp/example_icon.ico', format='ICO', sizes=[(256, 256)])