from PIL import Image, ImageDraw

# Define the size and colors
icon_size = (256, 256)
border_color = (0, 122, 204)  # A shade of blue
fill_color = (255, 255, 255)  # White
border_width = 10

# Create a new blank image with a white background
image = Image.new("RGBA", icon_size, fill_color)

# Create a draw object
draw = ImageDraw.Draw(image)

# Draw a rectangle for the border
draw.rectangle([0, 0, icon_size[0]-1, icon_size[1]-1], outline=border_color, width=border_width)

# Define the file path
file_path = "./tmp/backward_compatible_icon.ico"

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists("./tmp/"):
    os.makedirs("./tmp/")

# Save the image as an ICO file
image.save(file_path, format="ICO", sizes=[(256, 256)])

print(f"Icon saved to {file_path}")