from PIL import Image, ImageDraw
import os

def create_ico_file(color_depth, size=(256, 256), filename="icon"):
    """
    Creates an .ico file with the specified color depth.
    
    Parameters:
    - color_depth: The desired color depth (1, 8, 24, 32)
    - size: Tuple representing the width and height of the image
    - filename: Name of the file without extension
    """
    # Create an image with RGBA mode for 32-bit, RGB for 24-bit, P for 8-bit, and 1 for 1-bit.
    mode = "RGBA" if color_depth == 32 else "RGB" if color_depth == 24 else "P" if color_depth == 8 else "1"
    image = Image.new(mode, size)

    # Draw a simple shape to demonstrate transparency for 32-bit
    draw = ImageDraw.Draw(image)
    if color_depth == 32:
        draw.ellipse((0, 0, size[0], size[1]), fill=(255, 0, 0, 128))  # Semi-transparent red circle
    else:
        draw.ellipse((0, 0, size[0], size[1]), fill="red")  # Solid red circle for other depths

    # Ensure the output directory exists
    output_dir = "./tmp/"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the image as an .ico file
    file_path = os.path.join(output_dir, f"{filename}_{color_depth}bit.ico")
    image.save(file_path, format="ICO", sizes=[size])

# Create icons with different color depths
color_depths = [1, 8, 24, 32]
for depth in color_depths:
    create_ico_file(color_depth=depth)