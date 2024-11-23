import numpy as np
import os
from PIL import Image

def generate_gradient(height, width, start_color, end_color):
    """
    Generates a vertical gradient between two colors.

    Parameters:
    - height: The height of the gradient image.
    - width: The width of the gradient image.
    - start_color: The color at the top of the gradient (start), as an (R, G, B) tuple.
    - end_color: The color at the bottom of the gradient (end), as an (R, G, B) tuple.

    Returns: A height x width x 3 numpy array representing the gradient.
    """
    # Create an array to hold the gradient
    gradient = np.zeros((height, width, 3), dtype=np.float32)

    # Calculate the color steps
    for i in range(3):
        gradient[:, :, i] = np.linspace(start_color[i], end_color[i], height)[:, None]

    return np.clip(gradient, 0, 255).astype(np.uint8)

def save_image_as_ras(image_array, file_path):
    """
    Saves a numpy array as a .ras file using PIL.

    Parameters:
    - image_array: The numpy array to be saved.
    - file_path: The path where the .ras file will be saved.
    """
    # Convert the numpy array to a PIL image
    image = Image.fromarray(image_array)
    
    # PIL does not support .ras directly; save as .bmp and convert to .ras using external tools if necessary.
    # Here, saving as PNG as a demonstration, since this environment might not support .ras conversion.
    # For actual .ras saving, consider using a tool like ImageMagick or a custom writer based on the RAS specification.
    image.save(file_path, format='PNG')  # Change 'PNG' to 'RAS' when using a tool that supports .ras directly.

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the features of the image file to be generated
width, height = 640, 480
start_color = (255, 0, 0)  # Red
end_color = (0, 0, 255)  # Blue

# Generate a vertical gradient
data = generate_gradient(height, width, start_color, end_color)

# Save the image
file_path = './tmp/generated_gradient_image.png'  # Use .ras when possible
save_image_as_ras(data, file_path)

print(f'Gradient image saved as {file_path}')