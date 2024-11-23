import os
from PIL import Image

def apply_gamma_correction(image, gamma):
    """
    Applies gamma correction to a given image.
    
    :param image: An instance of PIL.Image.
    :param gamma: Gamma correction value.
    :return: Gamma corrected PIL.Image.
    """
    # Load pixel data
    pixels = image.load()
    width, height = image.size
    
    # Adjust the pixels for gamma correction
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (int((r / 255.0) ** gamma * 255),
                            int((g / 255.0) ** gamma * 255),
                            int((b / 255.0) ** gamma * 255))
    return image

def generate_gamma_corrected_images(start_gamma, end_gamma, step, width=800, height=600):
    """
    Generates a series of images with varying gamma correction levels and
    stores them in directories named after their gamma value.
    
    :param start_gamma: Starting gamma value.
    :param end_gamma: Ending gamma value.
    :param step: Step size for gamma value iteration.
    :param width: Width of the generated images.
    :param height: Height of the generated images.
    """
    # Ensure the base directory exists
    base_dir = './tmp/gamma_images/'
    os.makedirs(base_dir, exist_ok=True)
    
    gamma = start_gamma
    while gamma <= end_gamma:
        # Create a new image
        image = Image.new("RGB", (width, height), "white")
        # Apply gamma correction
        corrected_image = apply_gamma_correction(image, gamma)
        
        # Create a directory for the gamma value
        gamma_dir = os.path.join(base_dir, f"gamma_{gamma}/")
        os.makedirs(gamma_dir, exist_ok=True)
        
        # Save the gamma-corrected image
        file_path = os.path.join(gamma_dir, f"gamma_corrected_{gamma}.png")
        corrected_image.save(file_path, 'PNG')
        
        print(f"Gamma corrected image (gamma={gamma}) saved to {file_path}")
        
        # Increment gamma
        gamma += step

# Example usage
generate_gamma_corrected_images(0.5, 2.5, 0.5)