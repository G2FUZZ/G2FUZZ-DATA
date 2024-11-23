from PIL import Image, ImageDraw, ImageFont
import os

def create_pattern_image(pattern_type, size=(800, 600)):
    """Create an image with a specific pattern."""
    image = Image.new('RGB', size)
    draw = ImageDraw.Draw(image)
    
    if pattern_type == 'gradient':
        for i in range(size[1]):
            gradient_color = int(255 * (i / size[1]))
            draw.line([(0, i), (size[0], i)], fill=(gradient_color, gradient_color, 255))
    
    elif pattern_type == 'stripes':
        for i in range(0, size[0], 10):
            color = (255, 255, 255) if i % 20 == 0 else (0, 0, 0)
            draw.line([(i, 0), (i, size[1])], fill=color, width=10)
    
    elif pattern_type == 'dots':
        for x in range(0, size[0], 20):
            for y in range(0, size[1], 20):
                color = (255, 0, 0) if (x + y) % 40 == 0 else (0, 0, 255)
                draw.ellipse([x-5, y-5, x+5, y+5], fill=color)
    
    return image

def add_watermark_and_text(image, text="Complex Image Example", watermark_text="© Your Company"):
    """Add a semi-transparent watermark and text to the image."""
    draw = ImageDraw.Draw(image)
    size = image.size
    
    try:
        font = ImageFont.truetype("arial.ttf", 30)
    except IOError:
        font = ImageFont.load_default()
    
    draw.text((10, size[1] - 60), text, fill="white", font=font)
    
    watermark = Image.new('RGBA', size, (255, 255, 255, 0))
    watermark_draw = ImageDraw.Draw(watermark)
    watermark_draw.text((size[0]-200, size[1]-40), watermark_text, fill=(255, 255, 255, 128), font=font)
    
    image.paste(watermark, (0, 0), watermark)
    
    return image

def save_image_with_metadata(image, path, metadata={}):
    """Save the image with metadata."""
    # Directly save the image in JPEG format without attempting to add metadata using PngImagePlugin
    image.save(path, format='JPEG', quality=85)

def create_complex_images(save_path='./tmp/'):
    patterns = ['gradient', 'stripes', 'dots']
    for pattern in patterns:
        image = create_pattern_image(pattern)
        image = add_watermark_and_text(image, text=f"{pattern.capitalize()} Pattern Example")
        
        pattern_path = os.path.join(save_path, pattern)
        os.makedirs(pattern_path, exist_ok=True)
        
        filename = f"{pattern}_image.jpg"
        full_path = os.path.join(pattern_path, filename)
        
        metadata = {
            "Description": f"An example of an image with a {pattern} pattern."
        }
        save_image_with_metadata(image, full_path, metadata=metadata)

# Call the function to create and save the complex images
create_complex_images()