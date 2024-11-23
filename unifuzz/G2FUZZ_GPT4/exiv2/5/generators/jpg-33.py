import numpy as np
import cv2
import os

def create_gradient_image(width, height, direction='vertical'):
    """
    Create a gradient image of specified width and height.
    Direction can be 'vertical', 'horizontal', or 'diagonal'.
    """
    gradient = np.zeros((height, width, 3), dtype=np.uint8)
    if direction == 'vertical':
        for i in range(height):
            gradient[i, :, :] = [i, i, i] * (256 // height)
    elif direction == 'horizontal':
        for i in range(width):
            gradient[:, i, :] = [i, i, i] * (256 // width)
    elif direction == 'diagonal':
        for i in range(height):
            for j in range(width):
                gradient[i, j, :] = [(i+j)//2, (i+j)//2, (i+j)//2] * (256 // max(width, height))
    return gradient

def save_gradient_images(base_dir, qualities=[90, 70, 50, 30]):
    """
    Save gradient images in specified qualities and directions.
    """
    directions = ['vertical', 'horizontal', 'diagonal']
    # Ensure the base directory exists
    os.makedirs(base_dir, exist_ok=True)
    
    for quality in qualities:
        for direction in directions:
            # Create directory for each quality
            quality_dir = os.path.join(base_dir, f'{direction}', f'quality_{quality}')
            os.makedirs(quality_dir, exist_ok=True)

            # Generate gradient image
            gradient = create_gradient_image(256, 256, direction=direction)
            
            # File path
            file_path = os.path.join(quality_dir, f'{direction}_gradient_quality_{quality}.jpg')
            
            # Save the image
            cv2.imwrite(file_path, gradient, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
    
    print("Images generated and saved with varying qualities and directions.")

# Base directory for storing the images
base_dir = './tmp/complex_gradients'

save_gradient_images(base_dir)