from PIL import Image, ImageDraw
import os

def draw_pattern(image, mode):
    """Draw a simple pattern on the image based on its mode."""
    draw = ImageDraw.Draw(image)
    if mode in ['1', 'P', 'RGB', 'RGBA']:
        # Adjust color values for mode '1'
        outline_color = 255 if mode == '1' else (0, 128, 0)  # White for '1', green for others
        fill_color = 255 if mode == '1' else (255, 0, 0)  # White for '1', red for others
        
        # Draw a rectangle
        draw.rectangle([image.size[0]//4, image.size[1]//4, 3*image.size[0]//4, 3*image.size[1]//4], outline=outline_color, fill=fill_color)
        
        # Adjust line color for mode '1'
        line_color = 255 if mode == '1' else (0, 128, 0)  # White for '1', green for others
        
        # Draw a cross
        draw.line([0, 0, image.size[0], image.size[1]], fill=line_color, width=2)
        draw.line([0, image.size[1], image.size[0], 0], fill=line_color, width=2)
    return image

def create_icon_file(output_filename, color_depths, sizes):
    """Create an ICO file with images of multiple sizes and color depths."""
    icon_images = []
    for depth in color_depths:
        for size in sizes:
            # Determine the image mode based on color depth
            mode = '1' if depth == 1 else 'P' if depth in [4, 8] else 'RGB' if depth == 24 else 'RGBA'
            image = Image.new(mode, size)
            image = draw_pattern(image, mode)
            if mode == 'P':
                # Convert palette-based images (P) to RGB before adding
                image = image.convert('RGB')
            icon_images.append(image)
    
    # Save all images in the ICO file
    first_image = icon_images[0]
    first_image.save(output_filename, format='ICO', sizes=[(image.width, image.height) for image in icon_images], append_images=icon_images[1:])

# Ensure the output directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define color depths and sizes for demonstration
color_depths = [1, 4, 8, 24, 32]  # Bit depths
sizes = [(16, 16), (32, 32), (64, 64), (128, 128), (256, 256)]  # Icon sizes

# Generate a complex ICO file
output_filename = f'{output_dir}complex_icon.ico'
create_icon_file(output_filename, color_depths, sizes)

print("Complex ICO file has been generated.")