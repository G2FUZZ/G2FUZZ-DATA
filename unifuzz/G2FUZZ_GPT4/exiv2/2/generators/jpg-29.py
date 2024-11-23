from PIL import Image
import numpy as np
import os

def create_radial_gradient(width, height, colors):
    """
    Create an image with a radial gradient between two colors.
    colors: A tuple of two tuples, each representing the RGB values of the gradient's start and end color.
    """
    image = Image.new("RGB", (width, height))
    center_x, center_y = width / 2, height / 2
    max_radius = np.sqrt(center_x**2 + center_y**2)
    
    start_color, end_color = colors
    for x in range(width):
        for y in range(height):
            # Distance to the center
            distance = np.sqrt((center_x - x) ** 2 + (center_y - y) ** 2)
            # Calculate the current radius' proportion of the total radius
            radius_ratio = distance / max_radius
            
            # Interpolate between start and end colors based on the current radius ratio
            r = int(start_color[0] + (end_color[0] - start_color[0]) * radius_ratio)
            g = int(start_color[1] + (end_color[1] - start_color[1]) * radius_ratio)
            b = int(start_color[2] + (end_color[2] - start_color[2]) * radius_ratio)
            
            image.putpixel((x, y), (r, g, b))
    return image

def save_image_in_structure(image, base_dir, structure):
    """
    Save an image in a directory structure based on the specified structure.
    structure: A dictionary defining the directory structure and image characteristics.
    """
    # Construct the directory path
    dir_path = os.path.join(base_dir, *structure["path"])
    os.makedirs(dir_path, exist_ok=True)
    
    # Construct the file name
    file_name = f"{structure['name']}.jpg"
    file_path = os.path.join(dir_path, file_name)
    
    # Save the image
    image.save(file_path, 'JPEG', quality=structure.get("quality", 85))
    
    return file_path

# Example usage
width, height = 800, 600
colors = ((0, 128, 255), (255, 255, 0))  # Blue to yellow
image = create_radial_gradient(width, height, colors)

# Define the directory structure and image characteristics
structure = {
    "path": ["gradient_images", "radial", "blue_to_yellow"],
    "name": "radial_gradient",
    "quality": 90
}

# Save the image
base_dir = './tmp/'
file_path = save_image_in_structure(image, base_dir, structure)

print(f"Image saved to {file_path}")