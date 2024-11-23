from PIL import Image, ImageDraw, ImageFont
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate a blank image with PIL
img = Image.new('RGB', (400, 400), color = (255, 255, 255))

# Draw on the image
draw = ImageDraw.Draw(img)

# Draw multiple shapes
# Draw rectangles
draw.rectangle([30, 30, 170, 170], outline=(255, 0, 0), width=3)
draw.rectangle([230, 30, 370, 170], fill=(70, 130, 180), outline=(255, 0, 0), width=3)

# Draw ellipses
draw.ellipse([30, 230, 170, 370], outline=(0, 255, 0), width=3)
draw.ellipse([230, 230, 370, 370], fill=(123, 104, 238), outline=(0, 255, 0), width=3)

# Draw lines
draw.line([200, 0, 200, 400], fill=(0, 0, 0), width=2)
draw.line([0, 200, 400, 200], fill=(0, 0, 0), width=2)

# Add text
try:
    font = ImageFont.truetype("arial.ttf", 20)
except IOError:
    font = ImageFont.load_default()
    
draw.text((10, 10), "Shapes and Text", fill=(0, 0, 0), font=font)

# Save the image in JPEG format
complex_jpeg_path = os.path.join(output_dir, "complex_image.jpg")
img.save(complex_jpeg_path, "JPEG", quality=90)

print(f"Image saved at {complex_jpeg_path}")