from PIL import Image, ImageDraw

def create_hierarchical_image_with_variable_resolution(filename, size=(800, 600), resolution=(300, 300)):
    # Create the base image with the specified resolution
    base_image = Image.new('RGB', size, (255, 255, 255))
    base_image.info['dpi'] = resolution
    draw = ImageDraw.Draw(base_image)
    
    # Add some base content to the image
    draw.rectangle([10, 10, size[0]-10, size[1]-10], outline=(0, 0, 0), width=5)
    draw.text((20, 20), "Hierarchical Storage with Variable Resolution", fill=(0, 0, 0))
    
    # Function to recursively add smaller images
    def add_smaller_images(image, level=1, resolution_scaling_factor=1.5):
        if level > 3:  # Limit the recursion depth to avoid too many small images
            return image
        smaller_image_size = (int(image.width / 2), int(image.height / 2))
        smaller_image = image.copy().resize(smaller_image_size)
        
        # Adjust the DPI for the smaller image according to its level to simulate variable resolution
        dpi_scaling = resolution_scaling_factor ** level
        smaller_image.info['dpi'] = (int(resolution[0] * dpi_scaling), int(resolution[1] * dpi_scaling))
        
        image.paste(smaller_image, (image.width - smaller_image.width, image.height - smaller_image.height))
        return add_smaller_images(image, level + 1, resolution_scaling_factor)
    
    # Apply the smaller images onto the base image with variable resolutions
    final_image = add_smaller_images(base_image)
    
    # Save the image with the base resolution
    final_image.save(filename, dpi=resolution)

# Ensure the tmp directory exists
import os
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Create and save the hierarchical image with variable resolution
create_hierarchical_image_with_variable_resolution('./tmp/hierarchical_storage_variable_resolution.jpg')