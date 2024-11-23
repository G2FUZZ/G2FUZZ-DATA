import os
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

# Create the tmp directory if it doesn't exist
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create an image with white background
img = Image.new('RGB', (800, 600), color='white')
d = ImageDraw.Draw(img)

# Define header section
header_text = "PNG File Features"
header_bg_color = '#0A84FF'  # A blue color
header_font_size = 30
try:
    header_font = ImageFont.truetype("arial.ttf", header_font_size)
except IOError:
    header_font = ImageFont.load_default()

# Draw the header background
d.rectangle([0, 0, 800, 50], fill=header_bg_color)

# Add the header text
d.text((10, 10), header_text, fill=(255,255,255), font=header_font)

# Define the main text with multiple paragraphs
paragraphs = [
    "1. Transparency: PNG supports transparency, allowing the use of fade effects and varying levels of transparency.",
    "2. Interlacing: PNG's interlacing feature allows for an image to be loaded progressively, enhancing the user experience on slow connections.",
    "3. Color Depth: PNG supports a wide range of colors, from monochrome to 16 million colors, which is ideal for high-quality images."
]

paragraph_font_size = 15
try:
    paragraph_font = ImageFont.truetype("arial.ttf", paragraph_font_size)
except IOError:
    paragraph_font = ImageFont.load_default()

# Calculate the spacing and position for the paragraphs
current_height = 60
line_spacing = 5
for paragraph in paragraphs:
    d.text((10, current_height), paragraph, fill=(0,0,0), font=paragraph_font)
    current_height += paragraph_font_size + line_spacing

# Add an image watermark
watermark_path = 'watermark.png'  # Assume there's a watermark.png in the current directory
if os.path.exists(watermark_path):
    watermark = Image.open(watermark_path)
    if watermark.mode != 'RGBA':
        watermark = watermark.convert('RGBA')
    alpha = watermark.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(0.5)
    watermark.putalpha(alpha)
    img.paste(watermark, (img.width - 110, img.height - 110), watermark)

# Save the image as a PNG file
img.save(output_dir + 'complex_features.png')