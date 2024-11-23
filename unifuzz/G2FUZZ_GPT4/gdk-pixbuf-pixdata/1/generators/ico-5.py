from PIL import Image, ImageDraw
import os

def generate_adaptive_icons():
    # Create the ./tmp/ directory if it doesn't exist
    os.makedirs('./tmp/', exist_ok=True)

    # Define sizes for the adaptive icons (width, height)
    sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]

    # Create an empty list to store the image objects
    icons = []

    for size in sizes:
        # Create a new image with RGBA mode
        image = Image.new("RGBA", size, (255, 255, 255, 0))

        # Create a draw object
        draw = ImageDraw.Draw(image)

        # Define the rectangle properties
        rect_start = (size[0] * 0.25, size[1] * 0.25)
        rect_end = (size[0] * 0.75, size[1] * 0.75)
        rect_color = (0, 122, 204, 255)  # Blue rectangle

        # Draw a rectangle on the image
        draw.rectangle([rect_start, rect_end], fill=rect_color)

        # Append the image to the icons list
        icons.append(image)  # Changed here to append only the image

    # Save the icons as a multi-size .ico file
    ico_path = './tmp/adaptive_icon.ico'
    icons[0].save(ico_path, format='ICO', sizes=sizes)  # Changed here to use the sizes list directly

# Call the function
generate_adaptive_icons()