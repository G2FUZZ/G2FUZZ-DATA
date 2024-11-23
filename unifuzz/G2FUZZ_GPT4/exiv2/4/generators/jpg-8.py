from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def create_gradient_image(width, height, colors, filename, quality):
    """
    Creates a simple horizontal gradient image and saves it as a JPEG with specified compression quality.

    Parameters:
    - width: Width of the image
    - height: Height of the image
    - colors: A tuple of two colors to create the gradient between.
    - filename: The filename to save the image as.
    - quality: JPEG quality level (1-100)
    """
    # Create a new image with RGB mode
    image = Image.new("RGB", (width, height))
    
    # Create a draw object
    draw = ImageDraw.Draw(image)
    
    # Calculate gradient step
    r_step = (colors[1][0] - colors[0][0]) / width
    g_step = (colors[1][1] - colors[0][1]) / width
    b_step = (colors[1][2] - colors[0][2]) / width
    
    # Draw the gradient
    for i in range(width):
        r = int(colors[0][0] + r_step * i)
        g = int(colors[0][1] + g_step * i)
        b = int(colors[0][2] + b_step * i)
        draw.line((i, 0, i, height), fill=(r, g, b))
    
    # Save the image with specified quality
    image.save(filename, 'JPEG', quality=quality)

# Example usage

# Gradient from red to blue
colors = ((255, 0, 0), (0, 0, 255))

# Create and save the image with different compression levels
create_gradient_image(200, 100, colors, './tmp/gradient_high_quality.jpg', quality=95)
create_gradient_image(200, 100, colors, './tmp/gradient_low_quality.jpg', quality=25)