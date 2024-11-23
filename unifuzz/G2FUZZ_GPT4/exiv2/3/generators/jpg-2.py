from PIL import Image

def generate_gradient(width, height):
    """Generates a horizontal gradient from black to red, green, then blue."""
    gradient = Image.new('RGB', (width, height), color=0)
    for x in range(width):
        for y in range(height):
            # Cycle colors in the gradient from black to red, then green, then blue
            if x <= width // 3:
                color = (int(255 * (x / (width // 3))), 0, 0)  # Red gradient
            elif x <= 2 * width // 3:
                color = (0, int(255 * ((x - (width // 3)) / (width // 3))), 0)  # Green gradient
            else:
                color = (0, 0, int(255 * ((x - 2 * (width // 3)) / (width // 3))))  # Blue gradient
            gradient.putpixel((x, y), color)
    return gradient

def main():
    width, height = 800, 600  # Size of the image
    img = generate_gradient(width, height)
    # Ensure the ./tmp/ directory exists or create it with os.makedirs('./tmp/', exist_ok=True)
    img.save('./tmp/gradient_24bit.jpg', 'JPEG')

if __name__ == '__main__':
    main()