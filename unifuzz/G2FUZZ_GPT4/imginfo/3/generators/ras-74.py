from PIL import Image, ImageDraw, ImageFont
import os

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp', exist_ok=True)

# Define image size
width, height = 400, 400

# Create a new image with RGBA mode
image = Image.new("RGBA", (width, height))

# Initialize the drawing context
draw = ImageDraw.Draw(image)

# Create a vertical gradient
for i in range(height):
    gradient_color = (255, i % 256, 0, 128)
    draw.line((0, i, width, i), fill=gradient_color)

# Draw a rectangle with outline
draw.rectangle([50, 50, 350, 100], fill=(64, 204, 208, 255), outline=(255, 255, 255), width=2)

# Draw an ellipse
draw.ellipse([50, 150, 350, 300], fill=(255, 100, 100, 255), outline=(0, 0, 0))

# Prepare to draw text
try:
    # Attempt to use a default font
    font = ImageFont.truetype("arial.ttf", 36)
except IOError:
    # Fallback to a simpler font if the preferred font is unavailable
    font = ImageFont.load_default()

# Draw text
draw.text((50, 320), "Hello, World!", fill=(255, 255, 255, 128), font=font)

# Save the image as a PNG file
image.save("./tmp/complex_example.png")

# For RAS conversion, since PIL does not support saving as .ras directly,
# you would use external tools like ImageMagick, or convert manually.
# This step is outside the Python environment and thus not included in this script.