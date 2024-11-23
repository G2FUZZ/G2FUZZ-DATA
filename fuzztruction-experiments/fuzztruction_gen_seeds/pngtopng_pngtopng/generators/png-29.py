from PIL import Image, ImageDraw

def create_image_with_variable_opacity():
    # Image dimensions
    width, height = 800, 600
    
    # Create a new image with a white background and alpha channel for opacity
    image = Image.new('RGBA', (width, height), (255, 255, 255, 255))
    draw = ImageDraw.Draw(image)
    
    # Create rectangles of solid colors with varying opacity
    colors = [
        ('red', 255), # Opaque red
        ('green', 200), # Semi-transparent green
        ('blue', 150), # More transparent blue
        ('yellow', 100), # Very transparent yellow
        ('black', 50) # Nearly transparent black
    ]
    rectangle_width = width // len(colors)
    for i, (color, opacity) in enumerate(colors):
        # Convert color names to RGB and add opacity
        rgb_color = Image.new('RGBA', (1, 1), color).load()[0, 0][:3] + (opacity,)
        draw.rectangle([i * rectangle_width, 0, (i + 1) * rectangle_width, height], fill=rgb_color)
    
    # Save the image using PNG format to support opacity
    output_path = './tmp/variable_opacity_demo.png'
    image.save(output_path, 'PNG')

# Ensure the ./tmp/ folder exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

create_image_with_variable_opacity()