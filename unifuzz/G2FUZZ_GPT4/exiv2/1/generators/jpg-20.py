from PIL import Image, ImageDraw
import os
import cv2

# Create the directory for storing the images if it doesn't exist
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to degrade the image quality by re-saving it multiple times
def degrade_image_quality(initial_image_path, iterations=10):
    # Open the initial image
    image = Image.open(initial_image_path)
    
    # List to store paths of degraded images
    degraded_image_paths = []
    
    for i in range(iterations):
        # File path for the current iteration
        degraded_image_path = os.path.join(output_dir, f"degraded_{i+1}.jpg")
        
        # Save and re-open the image to simulate re-saving and degradation
        image.save(degraded_image_path, "JPEG", quality=90)  # Slightly reduce the quality to simulate edit & save
        image = Image.open(degraded_image_path)
        
        # Append the path of the degraded image to the list
        degraded_image_paths.append(degraded_image_path)
    
    return degraded_image_paths

# Function to create a Motion JPEG (M-JPEG) from the degraded images
def create_motion_jpeg(degraded_image_paths, output_file_name="motion_jpeg.avi", fps=1):
    # Assuming all images are the same size, open the first image to get the size
    img = cv2.imread(degraded_image_paths[0])
    height, width, layers = img.shape
    size = (width, height)

    # Define the codec and create VideoWriter object
    out = cv2.VideoWriter(output_file_name, cv2.VideoWriter_fourcc(*'MJPG'), fps, size)

    for filename in degraded_image_paths:
        img = cv2.imread(filename)
        out.write(img)

    out.release()

# Create an initial image
width, height = 800, 600
image = Image.new('RGB', (width, height), (255, 255, 255))
draw = ImageDraw.Draw(image)

# Optionally, add some text or graphics to make the degradation more noticeable
draw.text((10, 10), "Initial Image", fill=(0, 0, 0))

# Save the initial image
initial_image_path = os.path.join(output_dir, "initial_image.jpg")
image.save(initial_image_path)

# Call the function to degrade image quality
degraded_image_paths = degrade_image_quality(initial_image_path, iterations=10)

# Create a Motion JPEG (M-JPEG) from the degraded images
create_motion_jpeg(degraded_image_paths, output_file_name=os.path.join(output_dir, "motion_jpeg.avi"), fps=2)