from PIL import Image, ImageDraw, ImageFont
import os

def create_complex_image(output_path):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Create a new image with a white background
    image = Image.new('RGB', (400, 400), color=(255, 255, 255))

    # Initialize drawing context
    draw = ImageDraw.Draw(image)

    # Draw a simple rectangle
    draw.rectangle([10, 10, 100, 100], fill='blue')

    # Save the image
    image.save(output_path, 'JPEG')

    print(f"Image was saved at {output_path}")

# Ensure you're running this in the same environment where the function is defined
create_complex_image('./tmp/simple_image.jpg')