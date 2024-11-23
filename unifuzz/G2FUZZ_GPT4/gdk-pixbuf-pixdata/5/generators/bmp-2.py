import os
from PIL import Image

# Ensure the output directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Function to create a gradient image
def create_gradient_image(width, height, color_depth):
    # Create a new image with the specified color depth
    if color_depth == 1:
        mode = '1'  # 1 bit per pixel, black and white
    elif color_depth == 8:
        mode = 'P'  # 8 bits per pixel, palette-based
    elif color_depth == 24:
        mode = 'RGB'  # 24 bits per pixel, true color
    elif color_depth == 32:
        mode = 'RGBA'  # 32 bits per pixel, true color with alpha channel
    else:
        raise ValueError("Unsupported color depth")
    
    image = Image.new(mode, (width, height))
    
    # Draw a simple gradient or pattern
    for x in range(width):
        for y in range(height):
            if color_depth == 1:
                value = 255 * (x % 2)  # Simple black and white pattern
            elif color_depth == 8:
                value = (x + y) % 256  # Simple gradient in grayscale
            elif color_depth == 24:
                value = (x % 256, y % 256, (x + y) % 256)  # Color gradient
            elif color_depth == 32:
                value = (x % 256, y % 256, (x + y) % 256, x % 256)  # Color gradient with varying transparency
            image.putpixel((x, y), value)
    
    return image

# Create and save images with different color depths
for bits in [1, 8, 24, 32]:
    img = create_gradient_image(100, 100, bits)
    file_path = os.path.join(output_dir, f'gradient_{bits}bit.bmp')
    img.save(file_path)
    print(f"Image with {bits}-bit color depth saved to {file_path}")