from PIL import Image, ImageDraw, ImageFont

# Create an image with white background
img = Image.new('RGB', (800, 600), color = (255, 255, 255))

# Initialize the drawing context
draw = ImageDraw.Draw(img)

# Define the text to write for the features
text1 = "9. Standardization: The JPEG format (from which JPG files come) is standardized by the Joint Photographic Experts Group, ensuring consistent implementation across different platforms and devices."
text2 = "4. Arithmetic Coding Option: While less common due to patent restrictions (which have now expired), arithmetic coding is an alternative to the standard Huffman coding used in JPG compression, offering potentially more efficient compression."
text3 = "8. Multi-Picture Format (MPF): JPG files can support the Multi-Picture Format, which allows them to contain multiple images within a single file, useful for 3D photography or burst photos from digital cameras."

# Set the font and size
font = ImageFont.load_default()

# Position for the first text
text_x1, text_y1 = 10, 50

# Apply the first text to the image
draw.text((text_x1, text_y1), text1, fill=(0, 0, 0), font=font)

# Position for the second text (adjusted for spacing)
text_x2, text_y2 = 10, 150

# Apply the second text to the image
draw.text((text_x2, text_y2), text2, fill=(0, 0, 0), font=font)

# Position for the third text (adjusted for additional spacing)
text_x3, text_y3 = 10, 250

# Apply the third text to the image
draw.text((text_x3, text_y3), text3, fill=(0, 0, 0), font=font)

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image
img_path = './tmp/jpeg_features_with_mpf.jpg'
img.save(img_path)

print(f'Image saved to {img_path}')