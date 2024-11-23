from PIL import Image, ImageDraw
import os

def create_gradient_image(width, height, filename, quality=95):
    """
    Create a simple horizontal gradient image and save it with the specified quality.
    
    :param width: Width of the image.
    :param height: Height of the image.
    :param filename: Filename to save the image.
    :param quality: Quality for saving the image, affects the level of lossy compression.
    """
    # Ensure the tmp directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # Create a new image with RGB mode
    image = Image.new("RGB", (width, height))
    
    # Create a draw object
    draw = ImageDraw.Draw(image)
    
    # Generate gradient
    for i in range(width):
        # Calculate the color
        color = int(255 * (i / width))
        # Draw a line with the calculated color
        draw.line((i, 0, i, height), fill=(color, color, color))
    
    # Save the image with specified quality
    image.save(f'./tmp/{filename}.jpg', 'JPEG', quality=quality)

# Example usage:
create_gradient_image(500, 300, 'gradient_high_quality', quality=95)
create_gradient_image(500, 300, 'gradient_low_quality', quality=10)