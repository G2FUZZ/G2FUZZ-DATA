from PIL import Image, ImageDraw, ImageFont
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Create a new blank image
image = Image.new('RGB', (800, 600), color = (255, 255, 255))  # Adjusted the canvas size again for the extra content

# Initialize ImageDraw
draw = ImageDraw.Draw(image)

# Define the text to be drawn, including the new feature
text = """
6. Wide Compatibility: JPG is one of the most widely supported image formats, compatible with virtually all image viewing and editing software, as well as web browsers.

1. ICC Profile Support: JPG files can include ICC profiles to manage color across different devices, ensuring consistent color representation from the camera to the display screen.

6. JFIF and Exif Standards: JPG files often adhere to either the JFIF (JPEG File Interchange Format) or Exif (Exchangeable Image File Format) standards, which specify how metadata and image data are to be handled and stored.
"""

# Load a font
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # This path is an example; it might differ
try:
    font = ImageFont.truetype(font_path, 20)
except IOError:
    font = ImageFont.load_default()

# Drawing text on the image
draw.multiline_text((10, 10), text, fill=(0, 0, 0), font=font)

# Save the image
file_path = os.path.join(output_dir, 'features_including_jfif_exif_support.jpg')
image.save(file_path)

print(f"Image saved to {file_path}")