from PIL import Image, ImageDraw, ImageCms
import os

def create_image_with_text(size, text, bgcolor=(255, 255, 255), fgcolor=(0, 0, 0), color_space="RGB"):
    """Create an image with some text."""
    if color_space == "CMYK":
        image = Image.new("CMYK", size, color=bgcolor)
    else:
        image = Image.new("RGB", size, color=bgcolor)
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), text, fill=fgcolor)
    return image

def save_image_with_compression(image, path, quality=75):
    """Save an image with specified JPEG quality."""
    image.save(path, 'JPEG', quality=quality)

def generate_images_with_various_compressions_and_color_spaces(base_name, qualities=[10, 50, 90], color_spaces=["RGB", "CMYK"]):
    """Generate and save images with various levels of compression and color spaces."""
    os.makedirs('./tmp/', exist_ok=True)
    
    for color_space in color_spaces:
        for quality in qualities:
            image = create_image_with_text((200, 100), f'Quality: {quality}, {color_space}', color_space=color_space)
            filename = f'{base_name}_quality_{quality}_{color_space}.jpg'
            filepath = os.path.join('./tmp/', filename)
            save_image_with_compression(image, filepath, quality=quality)

generate_images_with_various_compressions_and_color_spaces('test_image')