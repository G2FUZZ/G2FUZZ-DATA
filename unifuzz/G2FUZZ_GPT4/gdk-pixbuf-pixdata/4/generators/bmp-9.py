from PIL import Image, ImagePalette
import os

def create_bmp_with_palette(color_depth):
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)

    # Define image size
    width, height = 100, 100

    # Create a new image with the specified color depth
    mode = 'P'  # Palette mode
    if color_depth == 1:
        # 2 colors for 1-bit
        colors = [(0, 0, 0), (255, 255, 255)]  # Black and white
    elif color_depth == 4:
        # 16 colors for 4-bit
        colors = [(i*16, i*16, i*16) for i in range(16)]  # Grayscale
    elif color_depth == 8:
        # 256 colors for 8-bit
        colors = [(i, i, i) for i in range(256)]  # Grayscale
    else:
        raise ValueError("Unsupported color depth")

    image = Image.new(mode, (width, height))
    palette = []
    for color in colors:
        palette.extend(color)
    image.putpalette(palette)

    # Draw a simple pattern: diagonal gradient based on the color depth
    pixels = image.load()
    for x in range(width):
        for y in range(height):
            if color_depth == 1:
                pixels[x, y] = (x + y) % 2  # Simple checkerboard pattern for 1-bit
            else:
                pixels[x, y] = (x + y) % len(colors)  # Diagonal gradient

    # Save the image
    file_name = f'./tmp/palette_{color_depth}bit.bmp'
    image.save(file_name, 'BMP')
    print(f"Image with {color_depth}-bit color depth and palette saved as {file_name}")

# Create BMP files for 1-bit, 4-bit, and 8-bit color depths
create_bmp_with_palette(1)
create_bmp_with_palette(4)
create_bmp_with_palette(8)