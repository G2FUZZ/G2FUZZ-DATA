import numpy as np
import cv2
import os

def create_complex_gradient_image(width, height, direction='vertical', pattern='gradient'):
    """
    Create a complex gradient image of specified width and height.
    Direction can be 'vertical', 'horizontal', or 'diagonal'.
    Pattern can be 'gradient' or 'checkerboard' to add complexity.
    """
    gradient = np.zeros((height, width, 3), dtype=np.uint8)

    # Generate base gradient
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

    # Add checkerboard pattern for complexity
    if pattern == 'checkerboard':
        for i in range(height):
            for j in range(width):
                if (i // 50) % 2 == (j // 50) % 2:
                    gradient[i, j, :] = 255 - gradient[i, j, :]

    return gradient

def apply_blur(image, intensity=5):
    """
    Apply Gaussian blur to the image based on the intensity.
    """
    blurred_image = cv2.GaussianBlur(image, (intensity*2+1, intensity*2+1), 0)
    return blurred_image

def add_text(image, text, position=(10, 25)):
    """
    Add text annotation to the image.
    """
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, text, position, font, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
    return image

def save_complex_gradient_images(base_dir, qualities=[90, 70, 50, 30]):
    """
    Save complex gradient images in specified qualities and directions with additional features.
    """
    directions = ['vertical', 'horizontal', 'diagonal']
    patterns = ['gradient', 'checkerboard']
    # Ensure the base directory exists
    os.makedirs(base_dir, exist_ok=True)
    
    for quality in qualities:
        for direction in directions:
            for pattern in patterns:
                # Create directory for each quality and pattern
                quality_pattern_dir = os.path.join(base_dir, f'{direction}', f'{pattern}', f'quality_{quality}')
                os.makedirs(quality_pattern_dir, exist_ok=True)

                # Generate complex gradient image
                gradient = create_complex_gradient_image(256, 256, direction=direction, pattern=pattern)
                
                # Apply Gaussian blur for lower qualities
                if quality <= 50:
                    gradient = apply_blur(gradient, intensity=5-quality//10)
                
                # Add text annotation
                gradient = add_text(gradient, f'{direction.capitalize()} {pattern}, Q={quality}')

                # File path
                file_path = os.path.join(quality_pattern_dir, f'{direction}_{pattern}_gradient_quality_{quality}.jpg')
                
                # Save the image
                cv2.imwrite(file_path, gradient, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
    
    print("Complex images generated and saved with varying qualities, directions, and patterns.")

# Base directory for storing the images
base_dir = './tmp/complex_gradients'

save_complex_gradient_images(base_dir)