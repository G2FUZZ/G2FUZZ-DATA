from PIL import Image, ImageDraw

def create_progressive_jpeg(filename):
    # Create a new image with RGB mode
    width, height = 800, 600
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)

    # Generate a vertical gradient
    for i in range(height):
        gradient_color = int(255 * (i / height))
        # Use gradient_color for the fill parameter
        draw.line([(0, i), (width, i)], fill=(gradient_color, gradient_color, gradient_color))

    # Ensure the ./tmp/ directory exists
    import os
    os.makedirs('./tmp/', exist_ok=True)

    # Save the image as a progressive JPEG
    image.save(f'./tmp/{filename}', 'JPEG', quality=80, progressive=True)

# Generate and save the image
create_progressive_jpeg('progressive_image.jpg')