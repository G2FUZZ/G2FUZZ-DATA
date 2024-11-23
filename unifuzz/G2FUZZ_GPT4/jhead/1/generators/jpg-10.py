from PIL import Image, ImageDraw, ImageFont
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Create an image with white background
width, height = 800, 200
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Define the text to be drawn
text = "10. Standardization: The format is standardized by the Joint Photographic Experts Group, ensuring consistent behavior across different platforms and devices."

# Load a font
try:
    # Try to load a default font
    font = ImageFont.truetype("arial.ttf", size=14)
except IOError:
    # If specific font is not found, use default PIL font
    font = ImageFont.load_default()

# Calculate text size and position
text_width, text_height = draw.textsize(text, font=font)
x = (width - text_width) / 2
y = (height - text_height) / 2

# Draw the text on the image
draw.text((x, y), text, fill="black", font=font)

# Save the image
output_path = os.path.join(output_dir, 'standardization.jpg')
image.save(output_path)

print(f"Image saved to {output_path}")