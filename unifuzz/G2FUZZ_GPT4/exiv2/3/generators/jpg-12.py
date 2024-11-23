import os
from PIL import Image, ImageDraw

# Create a directory for saving the images if it doesn't exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

def create_gradient_image(width, height, colors):
    """Create a gradient image from left to right."""
    base = Image.new('RGB', (width, height), colors[0])
    top = Image.new('RGB', (width, height), colors[1])
    mask = Image.new('L', (width, height))  # Adjusted to match the dimensions of the base and top images
    for y in range(height):  # Adjusted to fill the entire mask
        mask_data = [(int(255 * (x / width))) for x in range(width)]  # Use list comprehension for efficiency
        mask.putdata(mask_data, 0, y)  # Adjusted to fill each row of the mask
    base.paste(top, (0, 0, width, height), mask)
    return base

# Image settings
image_size = (800, 600)
gradient_colors = ('blue', 'red')

# Create a gradient image
image = create_gradient_image(image_size[0], image_size[1], gradient_colors)

# Save the image with different compression qualities including DCT feature
compression_levels = {'low': 10, 'medium': 50, 'high': 95, 'dct': 'keep'}
for quality_level, quality in compression_levels.items():
    file_path = os.path.join(output_dir, f'gradient_quality_{quality_level}.jpg')
    if quality_level == 'dct':
        image.save(file_path, 'JPEG', quality=95, subsampling=0, optimize=True)
    else:
        image.save(file_path, 'JPEG', quality=quality)

print("Images have been saved with different compression levels including DCT.")