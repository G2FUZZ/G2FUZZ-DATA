from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):  # Corrected variable name here
    os.makedirs(output_dir)

# Define image properties
image_width, image_height = 200, 200
background_color = "skyblue"
shape_color = "yellow"
rectangle_dimensions = [(50, 50), (150, 150)] # Top-left and bottom-right corners

# Create a new image with a solid color background
image = Image.new("RGB", (image_width, image_height), color=background_color)

# Draw a shape on the image
draw = ImageDraw.Draw(image)
draw.rectangle(rectangle_dimensions, fill=shape_color)

# Save the image as a GIF
gif_path = os.path.join(output_dir, "simple_shape.gif")
image.save(gif_path, "GIF")

print(f"Saved GIF to {gif_path}")