from PIL import Image, ImageDraw
import cv2
import numpy as np
import os

def create_hierarchical_image(filename, size=(800, 600)):
    # Create the base image
    base_image = Image.new('RGB', size, (255, 255, 255))
    draw = ImageDraw.Draw(base_image)
    
    # Add some base content to the image
    draw.rectangle([10, 10, size[0]-10, size[1]-10], outline=(0, 0, 0), width=5)
    draw.text((20, 20), "Hierarchical Storage", fill=(0, 0, 0))
    
    # Function to recursively add smaller images
    def add_smaller_images(image, level=1):
        if level > 3:  # Limit the recursion depth to avoid too many small images
            return image
        smaller_image = image.copy().resize((int(image.width / 2), int(image.height / 2)))
        image.paste(smaller_image, (image.width - smaller_image.width, image.height - smaller_image.height))
        return add_smaller_images(image, level + 1)
    
    # Apply the smaller images onto the base image
    final_image = add_smaller_images(base_image)
    
    # Save the image
    final_image.save(filename)

def create_motion_jpeg(filename, frame_count=30, size=(800, 600)):
    # Ensure the output directory exists
    output_dir = os.path.dirname(filename)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(filename, fourcc, 10.0, size)
    
    for _ in range(frame_count):
        # Create a frame
        frame_image = Image.new('RGB', size, (255, 255, 255))
        draw = ImageDraw.Draw(frame_image)
        draw.rectangle([10, 10, size[0]-10, size[1]-10], outline=(0, 0, 0), width=5)
        draw.text((20, 20), "Hierarchical Storage", fill=(0, 0, 0))
        frame_image = add_smaller_images(frame_image)
        
        # Convert PIL image to an array
        frame_array = np.array(frame_image)
        # Convert RGB to BGR
        frame_array = cv2.cvtColor(frame_array, cv2.COLOR_RGB2BGR)
        
        # Write the frame
        out.write(frame_array)
    
    # Release everything when job is finished
    out.release()

# Helper function to add smaller images (Refactored to be outside to be usable by both functions)
def add_smaller_images(image, level=1):
    if level > 3:  # Limit the recursion depth
        return image
    smaller_image = image.copy().resize((int(image.width / 2), int(image.height / 2)))
    image.paste(smaller_image, (image.width - smaller_image.width, image.height - smaller_image.height))
    return add_smaller_images(image, level + 1)

# Ensure the tmp directory exists
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Create and save the hierarchical image
create_hierarchical_image('./tmp/hierarchical_storage.jpg')

# Create and save the Motion JPEG (MJPEG) video
create_motion_jpeg('./tmp/hierarchical_storage_mjpeg.avi', frame_count=30, size=(800, 600))