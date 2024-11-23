from PIL import Image, ImageDraw, ImageFont
import os

def create_directory_structure(base_path, themes):
    """Create a directory structure based on the provided themes."""
    for theme in themes:
        dir_path = os.path.join(base_path, theme)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

def draw_gradient(draw, width, height, start_color, end_color):
    """Draw a vertical gradient between two colors."""
    for i in range(height):
        ratio = i / height
        r = int(start_color[0] * (1 - ratio) + end_color[0] * ratio)
        g = int(start_color[1] * (1 - ratio) + end_color[1] * ratio)
        b = int(start_color[2] * (1 - ratio) + end_color[2] * ratio)
        draw.line([(0, i), (width, i)], fill=(r, g, b))

def draw_shapes_and_text(image_path, gradient_colors, text, shape):
    """Draw an image with gradient, shapes and text."""
    image = Image.new('RGB', (400, 400))
    draw = ImageDraw.Draw(image)
    draw_gradient(draw, 400, 400, gradient_colors[0], gradient_colors[1])

    # Load font or use default if unavailable
    try:
        font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        font = ImageFont.truetype(font_path, 24)
    except IOError:
        font = None

    # Draw text
    draw.text((50, 50), text, fill='white', font=font)

    # Draw shape
    if shape == "rectangle":
        draw.rectangle([20, 150, 150, 200], outline="red", width=5)
    elif shape == "ellipse":
        draw.ellipse([200, 150, 350, 200], outline="white", width=5)
    elif shape == "line":
        draw.line([20, 250, 380, 250], fill="orange", width=3)

    # Save image
    image.save(image_path, 'JPEG', quality=95, progressive=True)

def generate_images(base_path, themes):
    """Generate a set of images based on themes."""
    for theme in themes:
        if theme == "nature":
            gradient_colors = ((34, 139, 34), (135, 206, 250)) # Forest green to sky blue
            text = "Nature"
            shape = "ellipse"
        elif theme == "urban":
            gradient_colors = ((105, 105, 105), (192, 192, 192)) # Dark grey to light grey
            text = "Urban"
            shape = "rectangle"
        else: # Default theme
            gradient_colors = ((255, 69, 0), (255, 215, 0)) # Red to yellow
            text = "Generic Theme"
            shape = "line"

        image_path = os.path.join(base_path, theme, "{}_image.jpg".format(theme))
        draw_shapes_and_text(image_path, gradient_colors, text, shape)

# Main execution
base_path = './tmp/themes'
themes = ['nature', 'urban', 'generic']
create_directory_structure(base_path, themes)
generate_images(base_path, themes)