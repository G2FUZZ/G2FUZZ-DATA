import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate an image of a specified color depth
def generate_bmp(color_depth):
    # Define image dimensions
    width, height = 256, 256

    # Create a new image with the specified color depth
    if color_depth in (1, 4, 8):
        mode = 'P'  # Indexed color: 1, 4, and 8 bits
    elif color_depth == 16:
        mode = 'RGB'  # 16-bit color can be simulated with a smaller color palette
        width, height = 64, 64  # Reduce size for simplicity in demonstration
    elif color_depth == 24:
        mode = 'RGB'  # 24-bit color (TrueColor)
    elif color_depth == 32:
        mode = 'RGBA'  # 32-bit color (TrueColor with Alpha)
    else:
        raise ValueError("Unsupported color depth")

    # Create a new image with a white background
    if color_depth in (1, 4, 8):
        image = Image.new(mode, (width, height), "white")
        pixels = image.load()
        for x in range(width):
            for y in range(height):
                pixels[x, y] = (x * y) % 255
        if color_depth == 1:
            image = image.convert('1')  # Convert to 1-bit color
    else:
        image = Image.new(mode, (width, height))
        pixels = image.load()
        for x in range(width):
            for y in range(height):
                red = (x % 256)
                green = (y % 256)
                blue = ((x + y) % 256)
                if color_depth == 32:
                    alpha = (x % 256)
                    pixels[x, y] = (red, green, blue, alpha)
                else:
                    pixels[x, y] = (red, green, blue)

    # Save the image
    filepath = f'./tmp/color_depth_{color_depth}.bmp'
    image.save(filepath)
    print(f"Image with color depth {color_depth} bpp saved to {filepath}")

# Generate BMP files for the specified color depths
for depth in [1, 4, 8, 16, 24, 32]:
    generate_bmp(depth)