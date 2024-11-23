from PIL import Image, ImageDraw, ImageFont

# Create an image with white background
img = Image.new('RGB', (800, 200), color = (255, 255, 255))

# Initialize the drawing context
draw = ImageDraw.Draw(img)

# Define the text to write
text = "9. Standardization: The JPEG format (from which JPG files come) is standardized by the Joint Photographic Experts Group, ensuring consistent implementation across different platforms and devices."

# Set the font and size
# For simplicity, using default font. For custom fonts, load them with ImageFont.truetype
font = ImageFont.load_default()

# Position for the text
text_x, text_y = 10, 50

# Apply the text to the image
draw.text((text_x, text_y), text, fill=(0, 0, 0), font=font)

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image
img_path = './tmp/jpeg_standardization.jpg'
img.save(img_path)

print(f'Image saved to {img_path}')