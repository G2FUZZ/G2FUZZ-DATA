from PIL import Image, ImageDraw, ImageFont, ImageOps
import os

# Ensure directory exists
def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Add border to an image
def add_border(input_image, border_size, color=0):
    if isinstance(input_image, Image.Image):
        img = ImageOps.expand(input_image, border=border_size, fill=color)
        return img
    else:
        raise ValueError("Input must be a PIL Image.")

# Draw multiline text
def draw_multiline_text(draw, text, position, font, max_width):
    lines = []
    words = text.split()
    while words:
        line = ''
        while words and font.getsize(line + words[0])[0] <= max_width:
            line += (words.pop(0) + ' ')
        lines.append(line)
    
    y_text = position[1]
    for line in lines:
        width, height = draw.textsize(line, font=font)
        draw.text(((max_width - width) / 2, y_text), line, font=font, fill="black")
        y_text += height

# Settings and initial setup
output_dir = "./tmp/"
ensure_dir(output_dir)

image_width, image_height = 800, 600
background_color = (255, 255, 255)

image = Image.new("RGB", (image_width, image_height), color=background_color)
draw = ImageDraw.Draw(image)

font_path = "arial.ttf"  # Adjust the font path as needed
try:
    font_large = ImageFont.truetype(font_path, 30)
    font_small = ImageFont.truetype(font_path, 20)
except IOError:
    font_large = ImageFont.load_default()
    font_small = ImageFont.load_default()

title_text = "Widespread Compatibility"
content_text = """JPG is one of the most widely supported image formats, compatible with virtually all image viewing and editing software, as well as web browsers. It's ideal for photographs and complex graphics."""

draw_multiline_text(draw, title_text, (0, 20), font_large, image_width)
draw_multiline_text(draw, content_text, (0, 60), font_small, image_width)

# Overlay an image (e.g., logo)
logo_path = "logo.png"  # Adjust the logo path as needed
try:
    logo = Image.open(logo_path).resize((100, 100))
    image.paste(logo, (image_width - 110, image_height - 110), logo)
except IOError:
    print("Logo file not found. Skipping overlay.")

# Add a border
border_size = 10
border_color = 'black'
image_with_border = add_border(image, border_size, border_color)

# Save the image
output_path = os.path.join(output_dir, "enhanced_image.jpg")
image_with_border.save(output_path)

print(f"Image saved to {output_path}")