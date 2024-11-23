from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def mandelbrot(c, max_iter):
    """Calculate the color of a Mandelbrot pixel."""
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def create_mandelbrot_image(width, height, filename, max_iter=100):
    """
    Creates an image of the Mandelbrot set.

    Parameters:
    - width: Width of the image
    - height: Height of the image
    - filename: The filename to save the image as.
    - max_iter: Maximum number of iterations to determine set membership
    """
    # Create a new image with RGB mode
    image = Image.new('RGB', (width, height))

    # Define the viewport
    x_min, x_max = -2.0, 1.0
    y_min, y_max = -1.5, 1.5
    
    # Convert pixel to complex coordinates
    for x in range(width):
        for y in range(height):
            c = complex(x_min + (x / width) * (x_max - x_min),
                        y_min + (y / height) * (y_max - y_min))

            # Calculate the color based on the iterations
            color = mandelbrot(c, max_iter)
            
            # Normalize and apply a color gradient
            image.putpixel((x, y), (255 - int(255 * color / max_iter), 
                                    int(255 * color / max_iter),
                                    255))

    # Save the image
    image.save(filename)

# Example usage

# Create and save the Mandelbrot set image
create_mandelbrot_image(800, 600, './tmp/mandelbrot.jpg', max_iter=100)