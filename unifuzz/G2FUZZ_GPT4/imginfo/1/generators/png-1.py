from PIL import Image, ImageDraw, ImageFont

# Create an image with white background
width, height = 800, 200
image = Image.new('RGBA', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Define the text and font (using a default PIL font)
text = "PNG uses a lossless compression algorithm that reduces file size without losing any image quality."
font = ImageFont.load_default()

# Calculate text width and height to center it
text_width, text_height = draw.textsize(text, font=font)
text_x = (width - text_width) / 2
text_y = (height - text_height) / 2

# Draw the text on the image
draw.text((text_x, text_y), text, fill='black', font=font)

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image
image_path = './tmp/lossless_compression_png.png'
image.save(image_path, 'PNG')

print(f"Image saved to {image_path}")