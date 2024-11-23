from PIL import Image, ImageDraw, ImageFont
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Gradient Image Creation
def create_gradient(width, height, left_color, right_color):
    base = Image.new('RGB', (width, height), left_color)
    top = Image.new('RGB', (base.width, base.height), right_color)
    mask = Image.new('L', (base.width, base.height))
    mask_data = []
    for y in range(base.height):
        mask_data.extend([int(255 * (x / base.width)) for x in range(base.width)])
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

gradient_image = create_gradient(100, 100, 'red', 'yellow')
gradient_image.save("./tmp/gradient_image.png")

# Transparent Image Creation
transparent_image = Image.new("RGBA", (100, 100))
for i in range(100):
    for j in range(50):
        transparent_image.putpixel((i, j), (255, 105, 180, 123))  # Pink with transparency
    for j in range(50, 100):
        transparent_image.putpixel((i, j), (0, 255, 255, 123))  # Cyan with transparency
transparent_image.save("./tmp/transparent_image.png")

# Image with Text Overlay
def draw_text(image, text, position, font_path=None, font_size=20, font_color="black"):
    draw = ImageDraw.Draw(image)
    if font_path is None:
        font = ImageFont.load_default()
    else:
        font = ImageFont.truetype(font_path, font_size)
    draw.text(position, text, fill=font_color, font=font)
    return image

# Create a simple image to draw text on
text_image = Image.new("RGB", (200, 100), "white")
text_image = draw_text(text_image, "Hello, World!", (10, 25), font_size=24, font_color="blue")
text_image.save("./tmp/text_image.png")