from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to create an image of specified color depth
def create_image(color_depth):
    # Create an image with a specific color depth
    if color_depth == 1:  # Monochrome
        mode = '1'  # 1-bit pixels, black and white
        file_name = './tmp/monochrome.ico'
    elif color_depth == 8:  # 256 colors
        mode = 'P'  # 8-bit pixels, mapped to any other mode using a color palette
        file_name = './tmp/256_colors.ico'
    else:  # 24-bit true color with 8-bit alpha
        mode = 'RGBA'  # 4x8-bit pixels, true color with transparency mask
        color_depth = 32  # Considering 24-bit color + 8-bit alpha
        file_name = './tmp/true_color_with_alpha.ico'

    # Image size
    size = (64, 64)

    # Create a new image with specified size and color depth
    image = Image.new(mode, size)

    # For demonstration, draw a simple element on the image
    # For monochrome, use 0 (black) or 255 (white)
    # For 8-bit color, use a value from 0 to 255 from the palette
    # For RGBA, use a tuple of (R, G, B, A)
    draw_color = 0 if mode == '1' else 255 if mode == 'P' else (255, 0, 0, 128)  # Red with half transparency for RGBA
    image.putpixel((32, 32), draw_color)  # Draw a single pixel in the center

    # Save the image as an .ico file with specified color depth
    image.save(file_name, format='ICO', sizes=[(64, 64)], bits=color_depth)

# Create images of different color depths
for depth in [1, 8, 32]:  # 32 here represents 24-bit color + 8-bit alpha
    create_image(depth)