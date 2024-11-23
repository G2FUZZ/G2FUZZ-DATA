from PIL import Image
import os

# Ensure the output directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define color depths and sizes for demonstration
color_depths = [1, 4, 8, 24, 32]  # Bit depths
sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]  # Icon sizes

# Generate icons
for depth in color_depths:
    for size in sizes:
        # Generate an image with the specified color depth and size
        if depth == 1:
            # Monochrome (1-bit)
            mode = '1'  # Black and white
        elif depth in [4, 8]:
            # Palette-based bit depths
            mode = 'P'
        elif depth == 24:
            # 24-bit true color (RGB)
            mode = 'RGB'
        else:
            # 32-bit true color with alpha (RGBA)
            mode = 'RGBA'
        
        # Create an image with the selected mode and size
        image = Image.new(mode, size)
        
        # Optional: Draw something on the image to make it distinct
        # For demonstration, we'll just fill it with a color
        if mode == '1':
            # Fill monochrome image with black (0) or white (255)
            image.paste(0, [0, 0, image.size[0], image.size[1]])
        elif mode in ['P', 'RGB', 'RGBA']:
            # Fill colored image with a color. Example here is red.
            # For 'P' (palette) images, convert to RGB first
            if mode == 'P':
                image = image.convert('RGB')
            color = (255, 0, 0) if mode in ['RGB', 'P'] else (255, 0, 0, 255)
            image.paste(color, [0, 0, image.size[0], image.size[1]])
        
        # Save the image as an ICO file
        filename = f'{output_dir}icon_{depth}bit_{size[0]}x{size[1]}.ico'
        image.save(filename, format='ICO', sizes=[size])

print("ICO files have been generated.")