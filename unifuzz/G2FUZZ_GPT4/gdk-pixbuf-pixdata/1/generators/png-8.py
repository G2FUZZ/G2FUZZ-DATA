import numpy as np
import matplotlib.pyplot as plt
import os

def create_gradient_image(width, height):
    """
    Create a simple gradient image for demonstration.
    """
    # Generate a gradient image
    x = np.linspace(0, 1, width)
    y = np.linspace(0, 1, height)
    X, Y = np.meshgrid(x, y)
    Z = (X**2 + Y**2) / 2  # Simple function to generate gradient

    return Z

def save_image(data, file_path):
    """
    Save the image data as a PNG file, using matplotlib to handle the PNG compression and filtering implicitly.
    """
    plt.imsave(file_path, data, cmap='viridis', format='png')

def main():
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)

    # Image dimensions and file path
    width, height = 256, 256
    file_path = './tmp/filter_algorithm_demo.png'

    # Create a gradient image
    gradient_image = create_gradient_image(width, height)

    # Save the image with applied filter algorithms (implicitly by the library)
    save_image(gradient_image, file_path)

    print(f"Image saved to {file_path}")

if __name__ == "__main__":
    main()