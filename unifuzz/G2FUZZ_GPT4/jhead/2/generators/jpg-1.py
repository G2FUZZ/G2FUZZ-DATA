from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def generate_gradient_image(width, height, start_color, end_color):
    """
    Generates a horizontal gradient image from start_color to end_color.
    """
    # Create an empty image
    image = Image.new("RGB", (width, height))
    left_color = np.array(start_color)
    right_color = np.array(end_color)
    
    # Calculate the color differences
    diff = right_color - left_color
    for x in range(width):
        # Calculate the current color
        current_color = left_color + (diff * (x / (width - 1)))
        # Draw a line with the current color
        line = [tuple(current_color.astype(int)) for y in range(height)]
        image.putdata(line, x, 0)
    
    return image

# Generate a gradient image
width, height = 800, 600
start_color = (255, 0, 0)  # Red
end_color = (0, 0, 255)  # Blue
gradient_image = generate_gradient_image(width, height, start_color, end_color)

# Save the image with different quality levels to illustrate lossy compression
gradient_image.save('./tmp/high_quality.jpg', 'JPEG', quality=95)
gradient_image.save('./tmp/medium_quality.jpg', 'JPEG', quality=50)
gradient_image.save('./tmp/low_quality.jpg', 'JPEG', quality=10)

print("JPEG files saved successfully demonstrating different levels of lossy compression.")