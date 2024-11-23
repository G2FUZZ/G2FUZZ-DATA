from PIL import Image, ImageDraw, ImageFont
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Create a new TIFF image
width, height = 800, 200
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Define text to be added
text = """
8. Interoperability: Due to its long-standing usage and versatility, TIFF files are supported by a wide variety of platforms and software, ensuring good interoperability across different systems and applications.
"""

# Optionally add a font
# For simplicity, we'll use PIL's default font here. For custom fonts, use ImageFont.truetype()
# font = ImageFont.truetype("arial.ttf", size=15)
font = ImageFont.load_default()

# Add text to image
draw.text((10, 10), text, fill="black", font=font)

# Save the image
file_path = os.path.join(output_dir, "interoperability_tiff.tiff")
image.save(file_path, format="TIFF")

print(f"TIFF file saved at: {file_path}")