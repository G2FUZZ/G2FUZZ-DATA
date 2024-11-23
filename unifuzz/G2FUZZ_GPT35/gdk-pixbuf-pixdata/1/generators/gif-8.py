from PIL import Image, ImageDraw, ImageFont
import os

# Create a directory for saving the generated GIF files
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with white background
width, height = 200, 200
image = Image.new('RGB', (width, height), 'white')

# Get a drawing context
draw = ImageDraw.Draw(image)

# Define the text to overlay
text = "Hello, GIF!"

# Load a font
font = ImageFont.load_default()

# Calculate text position
text_width, text_height = draw.textsize(text, font)
x = (width - text_width) // 2
y = (height - text_height) // 2

# Overlay text on the image
draw.text((x, y), text, fill='black', font=font)

# Save the image as a GIF file
image.save('./tmp/text_overlay.gif')

print("GIF file with text overlay has been generated and saved.")