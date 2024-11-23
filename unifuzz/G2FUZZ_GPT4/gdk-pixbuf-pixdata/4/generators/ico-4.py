from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Create a new image with RGBA (Red, Green, Blue, Alpha) mode
size = (256, 256)
image = Image.new("RGBA", size, (255, 255, 255, 0))

# Create a draw object to draw shapes and text
draw = ImageDraw.Draw(image)

# Draw a semi-transparent square with a border
border_color = (0, 0, 0, 255)  # Solid black
fill_color = (255, 0, 0, 128)  # Semi-transparent red
draw.rectangle([64, 64, 192, 192], outline=border_color, fill=fill_color)

# Draw a semi-transparent circle
circle_color = (0, 255, 0, 128)  # Semi-transparent green
draw.ellipse([96, 96, 160, 160], fill=circle_color)

# Save the image as an ICO file with alpha transparency
image.save("./tmp/icon_with_alpha.ico", format='ICO', sizes=[(256, 256)])

print("ICO file with alpha transparency has been saved to ./tmp/icon_with_alpha.ico")