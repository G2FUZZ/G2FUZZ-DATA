from PIL import Image, ImageDraw
import os

def generate_icon(sizes=[16, 32, 48, 64, 128, 256]):
    """
    Generate an ICO file with multiple sizes for scalability.

    Args:
    - sizes (list): List of sizes (in pixels) for the icon.
    """
    icon_images = []

    for size in sizes:
        # Create a new image with RGBA mode (transparency)
        image = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)

        # Draw a simple shape that scales with the image size
        # Here, we draw a circle that fills the image
        padding = size // 10
        draw.ellipse((padding, padding, size - padding, size - padding), fill=(255, 165, 0, 255))

        icon_images.append(image)

    # Ensure the ./tmp/ directory exists
    if not os.path.exists('./tmp/'):
        os.makedirs('./tmp/')

    # Save the icon with multiple sizes
    icon_filename = './tmp/scalable_icon.ico'
    icon_images[0].save(icon_filename, format='ICO', sizes=[(image.width, image.height) for image in icon_images])

generate_icon()