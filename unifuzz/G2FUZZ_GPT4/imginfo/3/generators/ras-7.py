from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a palette-based image (8-bit)
palette_image = Image.new('P', (100, 100))
palette_image.putpalette([
    0, 0, 0,  # Black
    255, 0, 0,  # Red
    0, 255, 0,  # Green
    0, 0, 255,  # Blue
    255, 255, 255  # White
] * 51)  # Extend the palette to the required size
draw = ImageDraw.Draw(palette_image)
draw.rectangle([10, 10, 90, 90], fill=1)  # Draw a red rectangle
draw.ellipse([25, 25, 75, 75], fill=2)  # Draw a green circle
palette_image_path = './tmp/palette_image.png'  # Changed to PNG
palette_image.save(palette_image_path)

# Generate a truecolor image (24-bit RGB)
truecolor_image = Image.new('RGB', (100, 100), "black")
draw = ImageDraw.Draw(truecolor_image)
draw.rectangle([10, 10, 90, 90], fill=(255, 0, 0))  # Draw a red rectangle
draw.ellipse([25, 25, 75, 75], fill=(0, 255, 0))  # Draw a green circle
truecolor_image_path = './tmp/truecolor_image.png'  # Changed to PNG
truecolor_image.save(truecolor_image_path)

print(f"Palette-based image saved to {palette_image_path}")
print(f"Truecolor image saved to {truecolor_image_path}")