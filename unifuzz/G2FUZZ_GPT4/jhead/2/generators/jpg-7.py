import os
from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
output_dir = "./tmp"
os.makedirs(output_dir, exist_ok=True)

# Create an image with a gradient
def create_gradient(width, height):
    image = Image.new("RGB", (width, height), "#FFFFFF")
    draw = ImageDraw.Draw(image)

    for i in range(width):
        gradient_color = int(255 * (i / width))
        draw.line((i, 0, i, height), fill=(gradient_color, gradient_color, gradient_color))

    return image

# Save the image with different compression levels
def save_with_compression_levels(image, path, base_filename):
    quality_levels = {'low': 10, 'medium': 50, 'high': 95}

    for name, quality in quality_levels.items():
        filename = f"{path}/{base_filename}_{name}.jpg"
        image.save(filename, 'JPEG', quality=quality)

# Main
if __name__ == "__main__":
    img = create_gradient(800, 600)
    save_with_compression_levels(img, output_dir, "gradient")