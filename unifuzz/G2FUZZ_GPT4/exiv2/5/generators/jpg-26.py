import numpy as np
import cv2
import os
from glob import glob

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def create_gradient_image(filename, width, height, quality):
    # Create a 256x256 gradient image
    gradient = np.zeros((height, width, 3), dtype=np.uint8)
    for i in range(height):
        value = i
        gradient[i, :, :] = [value, value, value]

    # Save the image with specified compression (quality)
    cv2.imwrite(filename, gradient, [int(cv2.IMWRITE_JPEG_QUALITY), quality])

def batch_process(source_dir, target_dir, quality):
    """
    Convert all images in the source directory to a different format or quality
    in the target directory.
    """
    os.makedirs(target_dir, exist_ok=True)
    image_files = glob(os.path.join(source_dir, '*'))
    
    for image_path in image_files:
        # Load the image
        image = cv2.imread(image_path)
        
        # Check if the image is loaded (i.e., not empty)
        if image is None or image.size == 0:
            print(f"Warning: Skipping file {image_path} as it could not be loaded as an image.")
            continue
        
        # Generate new file path in the target directory
        filename = os.path.basename(image_path)
        target_path = os.path.join(target_dir, filename)
        
        # Write image with new quality
        cv2.imwrite(target_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), quality])

# Example usage:

# Create a gradient image with low quality
create_gradient_image('./tmp/gradient_low_quality.jpg', 256, 256, 10)

# Batch process: Assuming there are other images in ./tmp/ to be processed
source_dir = './tmp/'
target_dir = './tmp/processed/'
batch_process(source_dir, target_dir, 50)

print("Image generated and saved with lossy compression. Batch processing completed.")