import numpy as np
from PIL import Image, ImageDraw
import json
import os

def create_image_with_transparency(width, height, transparency_level):
    """
    Creates an RGBA image with a given transparency level.
    """
    # Generate random colors
    data = np.random.rand(height, width, 3) * 255
    # Convert to uint8
    data = data.astype(np.uint8)
    # Create an RGBA image
    img = Image.fromarray(data, 'RGB')
    # Add an alpha channel with the specified transparency level
    alpha = Image.new('L', img.size, color=transparency_level)
    img.putalpha(alpha)
    return img

def merge_images(images):
    """
    Merges a list of images into a single composite image.
    """
    composite = Image.new('RGBA', images[0].size)
    for img in images:
        composite = Image.alpha_composite(composite, img)
    return composite

def create_complex_structure(width, height, num_layers):
    """
    Generates a series of images with varying levels of transparency and merges them.
    Saves the composite image and a JSON file with layer information.
    """
    # Ensure the ./tmp/ directory exists
    if not os.path.exists('./tmp/'):
        os.makedirs('./tmp/')
    
    images = []
    layer_info = []

    for i in range(num_layers):
        # Calculate transparency level for the layer
        transparency_level = int(255 / num_layers * (i + 1))
        img = create_image_with_transparency(width, height, transparency_level)
        images.append(img)
        # Save individual layer
        layer_filename = f'./tmp/layer_{i}.png'
        img.save(layer_filename)
        layer_info.append({
            'layer': i,
            'transparency': transparency_level,
            'file': layer_filename
        })

    # Merge images
    composite = merge_images(images)
    composite_filename = './tmp/composite_image.png'
    composite.save(composite_filename)

    # Save layer information
    with open('./tmp/layer_info.json', 'w') as f:
        json.dump(layer_info, f, indent=4)

    print(f"Composite image saved as {composite_filename}")
    print("Layer information saved in './tmp/layer_info.json'.")

# Parameters
width, height = 200, 200
num_layers = 5

# Generate the complex structure
create_complex_structure(width, height, num_layers)