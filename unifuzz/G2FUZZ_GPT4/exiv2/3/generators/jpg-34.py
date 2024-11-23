import os
from PIL import Image

def create_horizontal_gradient(width, height, colors):
    """Create a horizontal gradient image."""
    base = Image.new('RGB', (width, height), colors[0])
    top = Image.new('RGB', (width, height), colors[1])
    mask = Image.new('L', (width, height))
    for x in range(width):
        for y in range(height):
            mask.putpixel((x, y), int(255 * (x / width)))
    base.paste(top, (0, 0, width, height), mask)
    return base

def create_vertical_gradient(width, height, colors):
    """Create a vertical gradient image."""
    base = Image.new('RGB', (width, height), colors[0])
    top = Image.new('RGB', (width, height), colors[1])
    mask = Image.new('L', (width, height))
    for y in range(height):
        for x in range(width):
            mask.putpixel((x, y), int(255 * (y / height)))
    base.paste(top, (0, 0, width, height), mask)
    return base

def save_gradient_image(image, pattern, quality_level, output_dir):
    """Save the image with specified pattern and quality level."""
    directory = os.path.join(output_dir, pattern, quality_level)
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, f'gradient_{pattern}_{quality_level}.jpg')
    image.save(file_path, 'JPEG')
    print(f"Saved: {file_path}")

def main():
    # Image settings
    image_size = (800, 600)
    gradient_colors = ('blue', 'red')
    output_dir = './tmp/'
    patterns = {'horizontal': create_horizontal_gradient, 'vertical': create_vertical_gradient}
    compression_levels = {'low': 10, 'medium': 50, 'high': 95}

    for pattern_name, create_func in patterns.items():
        # Create a gradient image based on the pattern
        image = create_func(image_size[0], image_size[1], gradient_colors)
        
        for quality_level, quality in compression_levels.items():
            save_gradient_image(image, pattern_name, quality_level, output_dir)

main()