from PIL import Image, ImageDraw
import os

def create_gradient(width, height):
    """Create a simple gradient image"""
    gradient = Image.new('RGB', (width, height), color=0)
    draw = ImageDraw.Draw(gradient)
    
    for i in range(width):
        # Calculate the RGB values based on the position to create a gradient
        rgb = (int(255 * (i / width)), int(255 * (i / width)), 255)
        draw.line((i, 0, i, height), fill=rgb)
    
    return gradient

def save_with_compression_levels(image, path, quality_levels):
    """Save the image with different JPEG compression levels"""
    if not os.path.exists(path):
        os.makedirs(path)
    for quality in quality_levels:
        file_path = os.path.join(path, f"gradient_quality_{quality}.jpg")
        image.save(file_path, 'JPEG', quality=quality)

# Parameters
width, height = 800, 600
quality_levels = [10, 30, 50, 70, 90, 100]
path = './tmp'

# Create a gradient image
gradient_image = create_gradient(width, height)

# Save the image with different compression levels
save_with_compression_levels(gradient_image, path, quality_levels)

print("Images have been saved with different JPEG compression levels in './tmp/'.")