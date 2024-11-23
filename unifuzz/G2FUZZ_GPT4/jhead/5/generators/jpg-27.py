import numpy as np
from PIL import Image, ImageDraw
import os

def generate_radial_gradient(width, height):
    """
    Generate a radial gradient image where the color smoothly transitions from the center to the edges.
    """
    center_x, center_y = width / 2, height / 2
    max_radius = np.sqrt(center_x**2 + center_y**2)  # Maximum distance to a corner
    gradient_image = np.zeros((height, width, 3), dtype=np.uint8)
    
    for y in range(height):
        for x in range(width):
            distance_to_center = np.sqrt((x - center_x)**2 + (y - center_y)**2)
            ratio = distance_to_center / max_radius
            r = int(255 * (1 - ratio))  # Red decreases from center to edge
            g = int(255 * ratio)  # Green increases from center to edge
            b = 128  # Blue is constant for simplicity
            gradient_image[y, x] = [r, g, b]
    
    return gradient_image

def draw_concentric_circles(draw, center, max_radius, step, width):
    """
    Draw concentric circles with varying colors on the drawing context.
    """
    num_circles = int(max_radius / step)
    for i in range(num_circles):
        radius = (i + 1) * step
        color = (255 - i * 5 % 255, i * 7 % 255, i * 9 % 255)
        draw.ellipse([center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius], outline=color, width=width)

def create_image_with_complex_features(width, height):
    """
    Create an image with complex features such as concentric circles and a radial gradient.
    """
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # Generate a base radial gradient image
    gradient_image = generate_radial_gradient(width, height)
    img = Image.fromarray(gradient_image)
    draw = ImageDraw.Draw(img)
    
    # Add concentric circles with varying colors
    center = (width / 2, height / 2)
    max_radius = min(center)  # Use the smaller dimension for the maximum radius
    draw_concentric_circles(draw, center, max_radius, 20, 3)
    
    # Save the image
    img.save('./tmp/complex_gradient_image.jpg')
    print("Complex image saved successfully.")

# Parameters for the image
width, height = 800, 600
create_image_with_complex_features(width, height)