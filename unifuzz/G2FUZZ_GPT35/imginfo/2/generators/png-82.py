from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Create placeholder images
image1 = Image.fromarray(np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8))
image2 = Image.fromarray(np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8))

# Create a new image with a white background
image_combined = Image.new('RGB', (300, 200), color='white')

# Resize images if needed
image1 = image1.resize((100, 100))
image2 = image2.resize((100, 100))

# Paste images onto the combined image
image_combined.paste(image1, (50, 50))
image_combined.paste(image2, (150, 50))

# Add text annotation to the combined image
draw = ImageDraw.Draw(image_combined)
font = ImageFont.load_default()  # Use default font
draw.text((100, 170), "Complex PNG File", fill='black', font=font)

# Save the final combined image
image_combined.save('./tmp/complex_png.png')