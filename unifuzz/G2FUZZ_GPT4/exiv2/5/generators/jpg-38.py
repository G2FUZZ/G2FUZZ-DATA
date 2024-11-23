from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Create a new blank image
image = Image.new('RGB', (1200, 800), color = (255, 255, 255))

# Initialize ImageDraw
draw = ImageDraw.Draw(image)

# Define the text to be drawn, with different sections for different styles
texts = [
    {"content": "Wide Compatibility: One of the most widely supported formats.", "font_size": 24, "position": (20, 20)},
    {"content": "ICC Profile Support: Manages color across different devices.", "font_size": 18, "position": (20, 100)},
    {"specially_treated": True, "content": "Smoothing Filters: Applies filters to reduce artifacts.", "font_size": 18, "position": (20, 180)},
    {"content": "Grayscale Support: Stores images efficiently in monochrome.", "font_size": 18, "position": (20, 260)},
    {"content": "Arithmetic Coding Option: More efficient compression method.", "font_size": 18, "position": (20, 340)},
]

# Define base font path (this path is an example and might need to be adjusted)
font_path_base = "/usr/share/fonts/truetype/dejavu/DejaVuSans"

# Load different fonts
fonts = {
    18: ImageFont.truetype(f"{font_path_base}-Bold.ttf", 18),
    24: ImageFont.truetype(f"{font_path_base}.ttf", 24)
}

# Drawing text on the image with specific styles
for text_info in texts:
    font = fonts.get(text_info["font_size"], ImageFont.load_default())
    fill_color = (0, 0, 0)  # Default fill color
    
    # Check if the text section needs special treatment
    if text_info.get("specially_treated", False):
        # Enhance image section for this text
        brightness_enhancer = ImageEnhance.Brightness(image)
        image = brightness_enhancer.enhance(0.9)  # Slightly darken the image
        fill_color = (255, 105, 180)  # Change fill color for special treatment
    
    draw.multiline_text(text_info["position"], text_info["content"], fill=fill_color, font=font)

# Draw shapes (example: underline)
draw.line((20, 400, 400, 400), fill=(0, 0, 255), width=3)

# Add a watermark
try:
    watermark_font = ImageFont.truetype(f"{font_path_base}-Italic.ttf", 20)
except IOError:
    print("Italic font not found, falling back to default font.")
    watermark_font = ImageFont.load_default()

draw.text((1000, 780), "© 2023 Example Corp", fill=(180, 180, 180), font=watermark_font)

# Save the image
file_path = os.path.join(output_dir, 'features_extended_complexity.jpg')
image.save(file_path)

print(f"Image saved to {file_path}")