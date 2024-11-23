from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Create a new blank image
image = Image.new('RGBA', (800, 600), color = (255, 255, 255, 255))

# Initialize ImageDraw
draw = ImageDraw.Draw(image)

# Text sections with different styles
texts = [
    {"text": "6. Wide Compatibility: JPG is one of the most widely supported image formats.", "font_size": 20, "color": (76, 175, 80), "position": (10, 10)},
    {"text": "1. ICC Profile Support: Ensuring consistent color representation.", "font_size": 18, "color": (33, 150, 243), "position": (10, 60)},
    {"text": "4. Grayscale Support: Reducing file size significantly.", "font_size": 16, "color": (156, 39, 176), "position": (10, 100)},
    {"text": "5. Arithmetic Coding Option: More efficient but less common.", "font_size": 14, "color": (255, 87, 34), "position": (10, 140)}
]

# Load a default font and a specific font if available
default_font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
for text_info in texts:
    try:
        font = ImageFont.truetype(default_font_path, text_info["font_size"])
    except IOError:
        font = ImageFont.load_default()
    draw.text(text_info["position"], text_info["text"], fill=text_info["color"], font=font)

# Drawing shapes
draw.rectangle([(20, 180), (780, 230)], fill=(123, 31, 162), outline=(0, 0, 0))
draw.ellipse([(550, 250), (750, 450)], fill=(33, 150, 243), outline=(0, 0, 0))

# Adding transparency
overlay = Image.new('RGBA', image.size, (255, 255, 255, 0))
overlay_draw = ImageDraw.Draw(overlay)
overlay_draw.ellipse([(600, 300), (700, 400)], fill=(255, 193, 7, 128))
image = Image.alpha_composite(image, overlay)

# Applying a blur effect
image = image.filter(ImageFilter.GaussianBlur(2))

# Convert back to RGB to save as JPG
image = image.convert("RGB")

# Save the image
file_path = os.path.join(output_dir, 'complex_features_image.jpg')
image.save(file_path)

print(f"Image saved to {file_path}")