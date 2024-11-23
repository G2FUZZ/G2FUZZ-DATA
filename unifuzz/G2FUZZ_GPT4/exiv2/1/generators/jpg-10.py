from PIL import Image, ImageDraw, ImageFont
import os

# Create the directory for storing the images if it doesn't exist
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to degrade the image quality by re-saving it multiple times
def degrade_image_quality(initial_image_path, iterations=10):
    # Open the initial image
    image = Image.open(initial_image_path)
    
    for i in range(iterations):
        # File path for the current iteration
        degraded_image_path = os.path.join(output_dir, f"degraded_{i+1}.jpg")
        
        # Save and re-open the image to simulate re-saving and degradation
        image.save(degraded_image_path, "JPEG", quality=90)  # Slightly reduce the quality to simulate edit & save
        image = Image.open(degraded_image_path)

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
degrade_image_quality(initial_image_path, iterations=10)