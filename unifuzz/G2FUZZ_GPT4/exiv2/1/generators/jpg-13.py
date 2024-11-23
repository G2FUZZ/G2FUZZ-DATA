from PIL import Image, ImageDraw, ImageFont

# Create an image with white background
img = Image.new('RGB', (800, 400), color = (255, 255, 255))

# Initialize the drawing context
draw = ImageDraw.Draw(img)

# Define the text to write
text1 = "9. Standardization: The JPEG format (from which JPG files come) is standardized by the Joint Photographic Experts Group, ensuring consistent implementation across different platforms and devices."
text2 = "3. Chroma Subsampling: JPG often uses chroma subsampling, a process that reduces the color information in the image more than the luminance data, exploiting the human eye's lower sensitivity to fine color details, which helps to reduce file size with minimal impact on perceived quality."

# Set the font and size
# For simplicity, using default font. For custom fonts, load them with ImageFont.truetype
font = ImageFont.load_default()

# Position for the first text
text_x1, text_y1 = 10, 50

# Position for the second text, adjusting the y position based on the first text block
text_x2, text_y2 = 10, 150

# Apply the first text to the image
draw.text((text_x1, text_y1), text1, fill=(0, 0, 0), font=font)

# Apply the second text to the image
draw.text((text_x2, text_y2), text2, fill=(0, 0, 0), font=font)

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image
img_path = './tmp/jpeg_features.jpg'
img.save(img_path)

print(f'Image saved to {img_path}')