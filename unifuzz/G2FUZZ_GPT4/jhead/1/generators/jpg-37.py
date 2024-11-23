from PIL import Image, ImageDraw, ImageFont
import os

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Create a base image
base_img = Image.new('RGB', (400, 300), color=(73, 109, 137))

# Add a second layer to the image
top_img = Image.new('RGBA', (400, 300), (255, 255, 255, 128))  # Semi-transparent white layer
base_img.paste(top_img, (0, 0), top_img)

# Add text to the image
draw = ImageDraw.Draw(base_img)
font = ImageFont.load_default()  # Using default font
text = "Sample Text"
textwidth, textheight = draw.textsize(text, font)
# Positioning the text at the center
x = (base_img.width - textwidth) / 2
y = (base_img.height - textheight) / 2
draw.text((x, y), text, font=font, fill=(255, 0, 0))

# Path to your ICC profile
icc_profile_path = 'your_icc_profile_path.icc'

# Load an ICC profile
icc_profile = None
try:
    with open(icc_profile_path, 'rb') as f:
        icc_profile = f.read()
except IOError:
    print(f"ICC profile at {icc_profile_path} not found. Continuing without ICC profile.")

# Save the image with ICC profile, and as a high-quality JPEG
output_path = './tmp/complex_image.jpg'
base_img.save(output_path, 'JPEG', icc_profile=icc_profile, quality=95)
print("Complex image saved with additional features.")