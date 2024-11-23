import numpy as np
import cv2
import os

def generate_gradient_image(file_path, width, height, quality, scale=1.0):
    """
    Generates a gradient image of specified width and height, compresses it with a given quality,
    and saves it to the specified file path. It also allows for variable resolution through scaling.
    
    :param file_path: Path to save the image file.
    :param width: Width of the gradient image.
    :param height: Height of the gradient image.
    :param quality: JPEG quality for compression (0-100).
    :param scale: Scaling factor for variable resolution. Default is 1.0 (no scaling).
    """
    # Adjust dimensions according to the scaling factor
    scaled_width = int(width * scale)
    scaled_height = int(height * scale)
    
    # Create the gradient image
    gradient = np.zeros((scaled_height, scaled_width, 3), dtype=np.uint8)
    for i in range(scaled_height):
        value = int((i / scaled_height) * 255)  # Adjust gradient calculation for scaled size
        gradient[i, :, :] = [value, value, value]
    
    # Save the image with specified JPEG compression quality
    cv2.imwrite(file_path, gradient, [int(cv2.IMWRITE_JPEG_QUALITY), quality])

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Original image parameters
width, height = 256, 256
quality = 10  # Low quality

# Generate and save the original gradient image with low quality
generate_gradient_image('./tmp/gradient_low_quality.jpg', width, height, quality)

# Generate and save additional variations with variable resolutions
resolutions = [0.5, 1, 2]  # Example scaling factors for different resolutions
for scale in resolutions:
    file_name = f'./tmp/gradient_quality_{quality}_scale_{scale:.1f}.jpg'
    generate_gradient_image(file_name, width, height, quality, scale=scale)

print("Images generated and saved with various resolutions and lossy compression.")