from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def create_gradient_image_with_alpha(width, height, colors, filename, quality):
    """
    Creates a simple horizontal gradient image with an alpha channel and saves it as a JPEG 2000 which supports transparency.

    Parameters:
    - width: Width of the image
    - height: Height of the image
    - colors: A tuple of two colors to create the gradient between. Each color is a tuple of RGBA values.
    - filename: The filename to save the image as.
    - quality: JPEG 2000 quality level (1-100)
    """
    # Create a new image with RGBA mode
    image = Image.new("RGBA", (width, height))
    
    # Create a draw object
    draw = ImageDraw.Draw(image)
    
    # Calculate gradient steps
    r_step = (colors[1][0] - colors[0][0]) / width
    g_step = (colors[1][1] - colors[0][1]) / width
    b_step = (colors[1][2] - colors[0][2]) / width
    a_step = (colors[1][3] - colors[0][3]) / width  # Alpha step
    
    # Draw the gradient
    for i in range(width):
        r = int(colors[0][0] + r_step * i)
        g = int(colors[0][1] + g_step * i)
        b = int(colors[0][2] + b_step * i)
        a = int(colors[0][3] + a_step * i)  # Calculate alpha for current step
        draw.line((i, 0, i, height), fill=(r, g, b, a))
    
    # Save the image with specified quality in JPEG 2000 format which supports alpha
    image.save(filename, 'JPEG2000', quality_mode='dB', quality_layers=[quality])

# Example usage

# Gradient from red (transparent) to blue (opaque)
colors = ((255, 0, 0, 0), (0, 0, 255, 255))

# Create and save the image with alpha channel support
create_gradient_image_with_alpha(200, 100, colors, './tmp/gradient_with_alpha.jp2', quality=95)