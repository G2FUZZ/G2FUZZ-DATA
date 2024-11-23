import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_gradient(width, height, color1, color2):
    """Create a vertical gradient between two colors."""
    base = Image.new('RGB', (width, 1), color1)
    top = Image.new('RGB', (width, 1), color2)
    mask = Image.new('L', (width, 1))
    mask_data = []
    for y in range(width):
        mask_data.append(int(255 * (y / width)))
    mask.putdata(mask_data)
    gradient = Image.new('RGB', (width, height))
    for y in range(height):
        gradient.paste(base if y < height // 2 else top, (0, y))
    return gradient.filter(ImageFilter.GaussianBlur(radius=10))

def add_text(draw, text, position, font_path='arial.ttf', font_size=20, color=(255, 255, 255)):
    """Add text to an image."""
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()
    draw.text(position, text, fill=color, font=font)

def main(output_dir='./tmp/'):
    os.makedirs(output_dir, exist_ok=True)

    # Create an image with a gradient background
    width, height = 400, 300
    color1, color2 = (13, 2, 8), (100, 50, 200)  # Dark purple to light purple
    image = create_gradient(width, height, color1, color2)

    draw = ImageDraw.Draw(image)

    # Draw multiple shapes
    draw.ellipse([50, 50, 150, 150], fill=(255, 200, 0, 128), outline="yellow")
    draw.rectangle([250, 50, 350, 150], fill=(0, 255, 0, 128), outline="green")
    draw.polygon([(100, 200), (200, 250), (300, 200), (200, 150)], fill=(0, 0, 255, 128), outline="blue")

    # Add semi-transparent text
    add_text(draw, "Hello, World!", (60, 220), font_size=24, color=(255, 255, 255, 128))

    # Save the image
    file_path = os.path.join(output_dir, 'complex_image.png')
    image.save(file_path)

    print(f"Image saved to {file_path}")

if __name__ == "__main__":
    main()