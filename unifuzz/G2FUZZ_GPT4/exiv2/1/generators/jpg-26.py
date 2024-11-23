from PIL import Image, ImageDraw, ImageFont

# Create an image with white background
img = Image.new('RGB', (800, 400), color = (255, 255, 255))

# Initialize the drawing context
draw = ImageDraw.Draw(img)

# Define the text to write for JPEG feature
jpeg_text = "9. Standardization: The JPEG format (from which JPG files come) is standardized by the Joint Photographic Experts Group, ensuring consistent implementation across different platforms and devices."

# Define the text for SPIFF Header feature
spiff_text = "6. SPIFF Header: The Still Picture Interchange File Format (SPIFF) header is an alternative to the JFIF header, offering enhanced features for image categorization and compression type indication, though it is less commonly used."

# Set the font and size
# For simplicity, using default font. For custom fonts, load them with ImageFont.truetype
font = ImageFont.load_default()

# Position for the JPEG text
jpeg_text_x, jpeg_text_y = 10, 50

# Position for the SPIFF text, adjusting for the first text block
spiff_text_x, spiff_text_y = 10, 150

# Apply the JPEG feature text to the image
draw.text((jpeg_text_x, jpeg_text_y), jpeg_text, fill=(0, 0, 0), font=font)

# Apply the SPIFF Header feature text to the image
draw.text((spiff_text_x, spiff_text_y), spiff_text, fill=(0, 0, 0), font=font)

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image
img_path = './tmp/jpeg_with_spiff_header.jpg'
img.save(img_path)

print(f'Image saved to {img_path}')