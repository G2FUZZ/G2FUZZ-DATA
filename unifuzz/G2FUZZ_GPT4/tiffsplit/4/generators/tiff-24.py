from PIL import Image, ImageDraw, ImageFont
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Create a new TIFF image
width, height = 800, 400  # Increased height to accommodate additional text
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Define text to be added, now including "Image Defect Correction"
text = """
4. Image Defect Correction: TIFF format can store data related to image defect correction, allowing for the automatic correction of common image issues such as dust spots or optical aberrations in scanned images.

8. Interoperability: Due to its long-standing usage and versatility, TIFF files are supported by a wide variety of platforms and software, ensuring good interoperability across different systems and applications.
"""

# Optionally add a font
# For simplicity, we'll use PIL's default font here. For custom fonts, use ImageFont.truetype()
# font = ImageFont.truetype("arial.ttf", size=15)
font = ImageFont.load_default()

# Add text to image
draw.text((10, 10), text, fill="black", font=font)

# Save the image
file_path = os.path.join(output_dir, "features_tiff.tiff")
image.save(file_path, format="TIFF")

print(f"TIFF file saved at: {file_path}")