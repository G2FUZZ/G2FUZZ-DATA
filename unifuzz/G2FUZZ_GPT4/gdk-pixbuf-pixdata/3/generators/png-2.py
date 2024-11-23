import os
from PIL import Image, ImageDraw

# Create the tmp directory if it doesn't exist
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define image size and background color
image_size = (200, 200)
background_color = (255, 0, 0, 0)  # Fully transparent background

# Create a new image with RGBA mode for transparency support
image = Image.new("RGBA", image_size, background_color)

# Draw a semi-transparent circle
draw = ImageDraw.Draw(image)
circle_color = (0, 255, 0, 128)  # Semi-transparent green
circle_radius = 50
circle_position = (image_size[0] // 2, image_size[1] // 2)
draw.ellipse([circle_position[0] - circle_radius, circle_position[1] - circle_radius,
              circle_position[0] + circle_radius, circle_position[1] + circle_radius],
             fill=circle_color)

# Save the image
image.save(os.path.join(output_dir, 'transparent_image.png'))