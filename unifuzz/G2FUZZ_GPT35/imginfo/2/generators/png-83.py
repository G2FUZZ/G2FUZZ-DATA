from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Create placeholder images
image1 = Image.fromarray(np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8))
image2 = Image.fromarray(np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8))

# Create a new image with a white background and gradient fill
image_combined = Image.new('RGB', (300, 200), color='white')
draw = ImageDraw.Draw(image_combined)
for i in range(200):
    draw.line([(0, i), (300, i)], fill=(i, i, i))

# Resize images if needed
image1 = image1.resize((100, 100))
image2 = image2.resize((100, 100))

# Paste images onto the combined image
image_combined.paste(image1, (50, 50))
image_combined.paste(image2, (150, 50))

# Add text annotation to the combined image with a system font
default_font = ImageFont.load_default()
draw.text((100, 170), "Complex PNG File", fill='black', font=default_font)

# Draw shapes on the combined image
draw.rectangle([10, 10, 90, 90], outline='red', width=3)
draw.ellipse([160, 10, 240, 90], outline='blue', width=3)

# Save the final combined image
image_combined.save('./tmp/complex_png_extended.png')