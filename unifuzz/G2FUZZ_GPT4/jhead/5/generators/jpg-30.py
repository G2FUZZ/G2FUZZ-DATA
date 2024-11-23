from PIL import Image, ImageDraw, ImageFont
import os

# Ensure the ./tmp/ directory exists or create it
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

def draw_gradient(draw, width, height):
    """Draw a vertical gradient from blue to green"""
    for i in range(height):
        # Calculate the color
        ratio = i / height
        r = int(255 * (1 - ratio))
        g = 0
        b = int(255 * ratio)
        # Set the color for each pixel
        draw.line([(0, i), (width, i)], fill=(r, g, b))

# Create an image with a gradient background
image = Image.new('RGB', (400, 400))
draw = ImageDraw.Draw(image)

# Draw the gradient
draw_gradient(draw, 400, 400)

# Draw multiple layers of text with different sizes and colors
try:
    # Try to use a nicer font if available
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    font_size_big = 30
    font_size_small = 20
    font_big = ImageFont.truetype(font_path, font_size_big)
    font_small = ImageFont.truetype(font_path, font_size_small)
except IOError:
    # Fallback to default font
    font_big = None
    font_small = None

draw.text((50, 50), "Hello World!", fill='white', font=font_big)
draw.text((50, 100), "This is a more complex example.", fill='yellow', font=font_small)

# Draw shapes
draw.rectangle([20, 150, 150, 200], outline="red", width=5)
draw.ellipse([200, 150, 350, 200], outline="white", width=5)
draw.line([20, 250, 380, 250], fill="orange", width=3)

# Save the image as a high-quality progressive JPEG
image.save('./tmp/complex_image.jpg', 'JPEG', quality=95, progressive=True)