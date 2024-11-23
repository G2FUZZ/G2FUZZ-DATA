from PIL import Image, ImageDraw, ImageFont
import os

def create_complex_hierarchical_image(filename, size=(800, 600), resolution=(300, 300)):
    # Create the base image with the specified resolution
    base_image = Image.new('RGB', size, (255, 255, 255))
    base_image.info['dpi'] = resolution
    draw = ImageDraw.Draw(base_image)
    
    # Add some base content to the image
    draw.rectangle([10, 10, size[0]-10, size[1]-10], outline=(0, 0, 0), width=5)
    draw.text((20, 20), "Complex Hierarchical Storage", fill=(0, 0, 0))

    # Optionally, use a truetype font
    try:
        font = ImageFont.truetype("arial.ttf", 15)
    except IOError:
        font = ImageFont.load_default()
    
    # Function to recursively add smaller images with more complex structures
    def add_smaller_images(image, level=1, resolution_scaling_factor=1.5):
        if level > 3:
            return image
        smaller_image_size = (int(image.width / 2), int(image.height / 2))
        smaller_image = Image.new('RGB', smaller_image_size, (255, 255, 255))
        draw = ImageDraw.Draw(smaller_image)
        
        # Create a pattern based on the current level
        for i in range(0, smaller_image_size[0], 20):
            color = (255, 0, 0) if i % 40 == 0 else (0, 255, 0)
            draw.line((i, 0, i, smaller_image_size[1]), fill=color, width=1)
        
        # Add text to the smaller image
        text_msg = f"Level {level}"
        draw.text((10, 10), text_msg, fill=(0, 0, 255), font=font)
        
        # Adjust the DPI for the smaller image according to its level to simulate variable resolution
        dpi_scaling = resolution_scaling_factor ** level
        smaller_image.info['dpi'] = (int(resolution[0] * dpi_scaling), int(resolution[1] * dpi_scaling))
        
        image.paste(smaller_image, (image.width - smaller_image.width, image.height - smaller_image.height))
        return add_smaller_images(image, level + 1, resolution_scaling_factor)
    
    # Apply the smaller images with complex structures onto the base image
    final_image = add_smaller_images(base_image)
    
    # Save the image with the base resolution
    final_image.save(filename, dpi=resolution)

# Ensure the tmp directory exists
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Create and save the complex hierarchical image
create_complex_hierarchical_image('./tmp/complex_hierarchical_storage.jpg')