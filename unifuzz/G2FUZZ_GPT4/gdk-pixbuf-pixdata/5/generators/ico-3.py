from PIL import Image, ImageDraw
import os

def create_icon(size):
    # Create a new image with a white background
    img = Image.new('RGBA', (size, size), "white")
    draw = ImageDraw.Draw(img)

    # Draw a simple shape, for example, a red circle at the center
    draw.ellipse((size * 0.25, size * 0.25, size * 0.75, size * 0.75), fill="red")

    return img

def save_icons(sizes, directory):
    os.makedirs(directory, exist_ok=True)

    icon_images = []
    for size in sizes:
        img = create_icon(size)
        icon_images.append(img)

    # PIL allows saving multiple sizes in a single ICO file
    first_image = icon_images.pop(0)
    first_image.save(os.path.join(directory, 'generated_icon.ico'), format='ICO', sizes=[(img.width, img.height) for img in [first_image] + icon_images])

sizes = [16, 32, 48, 64, 128, 256]
save_icons(sizes, './tmp/')