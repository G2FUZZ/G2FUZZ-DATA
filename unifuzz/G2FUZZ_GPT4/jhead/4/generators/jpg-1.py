import numpy as np
import cv2
import os

def create_gradient_image(width, height, start_color, end_color):
    """
    Create a gradient image from start_color to end_color.

    Parameters:
    - width: Width of the image
    - height: Height of the image
    - start_color: Starting color of the gradient (BGR tuple)
    - end_color: Ending color of the gradient (BGR tuple)

    Returns:
    - A numpy array representing the gradient image.
    """
    # Create an array with the shape of the image, filled with the starting color
    image = np.tile(np.linspace(start_color, end_color, width), (height, 1, 1))
    return image.astype(np.uint8)

def save_compressed_jpeg(image, path, quality):
    """
    Save the image as a JPEG file with specified quality.

    Parameters:
    - image: The image to save
    - path: Path where the image will be saved
    - quality: Quality for the JPEG file (0-100)
    """
    cv2.imwrite(path, image, [int(cv2.IMWRITE_JPEG_QUALITY), quality])

def main():
    # Create a directory for saving the images
    output_dir = './tmp/'
    os.makedirs(output_dir, exist_ok=True)

    # Image dimensions and gradient colors (BGR format)
    width, height = 800, 600
    start_color = (0, 0, 0)  # Black
    end_color = (255, 255, 255)  # White

    # Create a gradient image
    gradient_image = create_gradient_image(width, height, start_color, end_color)

    # Save the image with different compression qualities
    for quality in [95, 75, 50, 25, 10]:
        output_path = os.path.join(output_dir, f'gradient_compression_{quality}.jpg')
        save_compressed_jpeg(gradient_image, output_path, quality)
        print(f'Saved {output_path} with quality {quality}')

if __name__ == "__main__":
    main()