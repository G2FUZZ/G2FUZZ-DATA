from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an image with RGB encoding
img_rgb = Image.new('RGB', (100, 100), color = 'red')
img_rgb.save('./tmp/img_rgb.png', 'PNG')

# Create an image with RGBA encoding
img_rgba = Image.new('RGBA', (100, 100), color = (0, 0, 255, 128))  # Corrected color specification
img_rgba.save('./tmp/img_rgba.png', 'PNG')

# Create an image with grayscale encoding
img_gray = Image.new('L', (100, 100), color = 'gray')
img_gray.save('./tmp/img_gray.png', 'PNG')

# Create an image with CMYK encoding
img_cmyk = Image.new('CMYK', (100, 100), color = 'magenta')

# Convert CMYK to RGB before saving as PNG
img_cmyk_rgb = img_cmyk.convert("RGB")
img_cmyk_rgb.save('./tmp/img_cmyk.png', 'PNG')