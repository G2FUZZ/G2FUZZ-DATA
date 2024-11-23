from PIL import Image, ImageDraw, ImageFont
import os

def create_advanced_pgx_image(directory='./tmp/', filename='advanced_image.pgx', size=(256, 256), color=(128, 128, 128), mode='RGB', text=None, shapes=[]):
    """
    Create a PGX file containing an image with additional features like text and shapes.

    Parameters:
    - directory: The directory to save the PGX file.
    - filename: The name of the PGX file.
    - size: A tuple (width, height) specifying the size of the image.
    - color: The color value to fill the image. This can be a single integer for grayscale or a tuple for RGB.
    - mode: The color mode of the image ('L' for grayscale or 'RGB').
    - text: A tuple containing (text, position, font path, font size, font color) to add text overlays. Example: ("Hello", (10, 10), "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24, (255, 70, 70))
    - shapes: A list of tuples specifying shapes to draw. Each tuple contains (shape type, position, width, color). Example: [("line", (0, 0, 100, 100), 2, (255, 0, 0))]
    """
    # Ensure the target directory exists
    os.makedirs(directory, exist_ok=True)
    
    # Create a new image with the specified size, color, and mode
    img = Image.new(mode, size, color)
    draw = ImageDraw.Draw(img)
    
    # Add text if specified
    if text:
        text_content, position, font_path, font_size, font_color = text
        try:
            font = ImageFont.truetype(font_path, font_size)
        except IOError:
            print(f"Warning: Could not load font at {font_path}. Using default font.")
            font = ImageFont.load_default()
        draw.text(position, text_content, fill=font_color, font=font)
    
    # Draw shapes if specified
    for shape in shapes:
        shape_type, shape_position, line_width, shape_color = shape
        if shape_type == "line":
            draw.line(shape_position, fill=shape_color, width=line_width)
        elif shape_type == "rectangle":
            draw.rectangle(shape_position, outline=shape_color, width=line_width)
    
    # Define the full path for the PGX file
    filepath = os.path.join(directory, filename)
    
    # Save the image in PGX format
    img.save(filepath, format='JPEG2000', quality_mode='dB', quality_layers=[80])

    print(f"Advanced PGX file saved at: {filepath}")

# Example usage
create_advanced_pgx_image(
    text=("Sample Text", (50, 50), "arial.ttf", 20, (255, 255, 255)),
    shapes=[("line", (10, 10, 100, 100), 3, (255, 0, 0)), ("rectangle", (110, 10, 210, 110), 2, (0, 255, 0))]
)