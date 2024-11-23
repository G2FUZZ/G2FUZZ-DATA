from PIL import Image, ImageCms, ImageDraw, ImageFont, PngImagePlugin
import os

def create_gradient_image(width, height, start_color, end_color, orientation='vertical'):
    """
    Creates an image with a gradient filling between `start_color` and `end_color`.
    Supports both vertical and horizontal gradients.
    """
    base = Image.new('RGB', (width, height), start_color)
    top_color = Image.new('RGB', (1, 1), end_color).getpixel((0, 0))

    for i in range(base.size[0] if orientation == 'horizontal' else base.size[1]):
        # Calculate the intermediate color at this point
        intermediate_color = tuple(
            int(start_color[j] + (float(i) / (base.size[0 if orientation == 'horizontal' else 1] - 1)) * (top_color[j] - start_color[j]))
            for j in range(3)
        )
        for x in range(width) if orientation == 'vertical' else range(height):
            base.putpixel((x, i) if orientation == 'vertical' else (i, x), intermediate_color)

    return base

def add_text_overlay(image, texts, font_path, default_font_size=20, default_color='white'):
    """
    Adds multiple text overlays to an existing image.
    `texts` is a list of tuples containing (text, position, font_size, color).
    """
    draw = ImageDraw.Draw(image)
    for text, position, font_size, color in texts:
        font = ImageFont.truetype(font_path, font_size)
        draw.text(position, text, font=font, fill=color)
    return image

def add_shapes(image, shapes):
    """
    Adds geometric shapes to an existing image.
    `shapes` is a list of tuples describing shapes to draw, where each tuple contains
    (shape_type, bounding_box, outline_color, fill_color).
    """
    draw = ImageDraw.Draw(image)
    for shape in shapes:
        shape_type, bounding_box, outline_color, fill_color = shape
        if shape_type == 'rectangle':
            draw.rectangle(bounding_box, outline=outline_color, fill=fill_color)
        elif shape_type == 'ellipse':
            draw.ellipse(bounding_box, outline=outline_color, fill=fill_color)
    return image

def add_pattern_fill(image, pattern_image, pattern_alpha=128):
    """
    Fills the entire image with a repeating pattern.
    `pattern_image` is a small image to be repeated across the main image.
    `pattern_alpha` controls the opacity of the pattern overlay.
    """
    pattern = pattern_image.copy()
    pattern.putalpha(pattern_alpha)

    for x in range(0, image.width, pattern.width):
        for y in range(0, image.height, pattern.height):
            image.paste(pattern, (x, y), pattern)
    return image

def add_metadata(image, metadata):
    """
    Adds custom metadata to an image.
    """
    meta = PngImagePlugin.PngInfo()
    for key, value in metadata.items():
        meta.add_text(key, value)
    image.info["pnginfo"] = meta
    return image

# Example Workflow
width, height = 800, 600
background_layer = create_gradient_image(width, height, (64, 64, 64), (0, 0, 0), 'horizontal')
pattern_layer = Image.new('RGB', (50, 50), (255, 255, 255))
pattern_layer = add_shapes(pattern_layer, [('ellipse', (0, 0, 50, 50), None, 'blue')])

# Add pattern fill and shapes
image_with_pattern = add_pattern_fill(background_layer, pattern_layer, 64)
image_with_shapes = add_shapes(image_with_pattern, [
    ('rectangle', (50, 50, 750, 550), 'red', None),
    ('ellipse', (200, 150, 600, 450), 'green', None)
])

# Add multiple text overlays
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
texts = [
    ("Complex Structure", (300, 20), 30, 'yellow'),
    ("Multiple Texts", (300, 520), 25, 'white')
]
composite_image_with_text = add_text_overlay(image_with_shapes, texts, font_path)

# Add metadata
metadata = {"Description": "This is a complex image structure with patterns and shapes", "Author": "Your Name"}
image_with_metadata = add_metadata(composite_image_with_text, metadata)

# Ensure the './tmp/' directory exists
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Save the image
image_with_metadata.save(
    "./tmp/complex_patterned_image.jpg",
    "JPEG",
    dpi=(300, 300),
    quality=95
)

print("Complex image with patterns, shapes, and text overlays saved at './tmp/complex_patterned_image.jpg'")