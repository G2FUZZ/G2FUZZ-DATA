from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

def create_gradient(width, height):
    """Create a gradient image from black to white."""
    base = Image.new('RGB', (width, height), "black")
    draw = ImageDraw.Draw(base)

    for i in range(width):
        color = int(255 * (i / width))  # Gradient from black to white
        draw.line((i, 0, i, height), fill=(color, color, color))

    return base

def demonstrate_lossy_compression(image, iterations=5):
    """Demonstrate lossy compression by repeatedly saving and reloading a JPG."""
    path = os.path.join(output_dir, 'gradient.jpg')
    image.save(path, 'JPEG', quality=95)  # Initial save with high quality

    for i in range(iterations):
        # Reopen and resave the image to progressively reduce its quality
        image = Image.open(path)
        image.save(path, 'JPEG', quality=95)  # Resaving with high quality to simulate quality loss over iterations

    image.show()  # Optionally show the final image

# Create a gradient image
gradient_image = create_gradient(500, 300)

# Demonstrate the effect of lossy compression
demonstrate_lossy_compression(gradient_image)
