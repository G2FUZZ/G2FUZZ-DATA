from PIL import Image
import numpy as np
import os

def generate_gradient_image(width, height, start_color, end_color):
    """
    Generates a simple horizontal gradient between two colors.
    """
    # Create an array of the start color
    base = np.tile(np.linspace(start_color, end_color, width), (height, 1))
    # Stack to get RGB image
    return np.dstack([base] * 3)

def save_image_with_compression(image_array, path, compression_level):
    """
    Saves an image with a specific JPEG compression level.
    """
    image = Image.fromarray(np.uint8(image_array))
    image.save(path, quality=compression_level)

def main():
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)

    # Generate a gradient image
    width, height = 800, 600
    start_color, end_color = 0, 255  # Black to white
    image_array = generate_gradient_image(width, height, start_color, end_color)

    # Save with different compression levels
    compression_levels = [95, 50, 10]  # High, medium, and low quality
    for level in compression_levels:
        filename = f'./tmp/gradient_compression_{level}.jpg'
        save_image_with_compression(image_array, filename, level)

    print("Images have been saved with different compression levels.")

if __name__ == "__main__":
    main()