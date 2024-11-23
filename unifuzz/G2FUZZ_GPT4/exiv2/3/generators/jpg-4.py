from PIL import Image, ImageDraw
import os

def create_progressive_jpeg(filename, width=100, height=100):
    # Create a new image with white background
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)

    # Draw a simple element; here a red rectangle
    draw.rectangle([width // 4, height // 4, 3 * width // 4, 3 * height // 4], fill="red")

    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)

    # Save the image as progressive JPEG
    img.save(f'./tmp/{filename}', 'JPEG', quality=95, progressive=True)

# Generate a progressive JPEG image
create_progressive_jpeg('progressive_image.jpg')