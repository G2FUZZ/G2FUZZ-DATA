import os
from PIL import Image
import numpy as np

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define image properties
color_models = {
    'RGB': {'mode': 'RGB', 'size': (100, 100), 'color': (255, 0, 0)},  # Red in RGB
    'CMYK': {'mode': 'CMYK', 'size': (100, 100), 'color': (0, 255, 255, 0)},  # Equivalent red in CMYK
    'Grayscale': {'mode': 'L', 'size': (100, 100), 'color': 128}  # Medium gray in Grayscale
}

# Generate images for each color model
for model_name, properties in color_models.items():
    # Create an image for the current color model
    if model_name == 'RGB' or model_name == 'Grayscale':
        img = Image.new(properties['mode'], properties['size'], color=properties['color'])
    elif model_name == 'CMYK':
        # For CMYK, create an array and then convert it to an Image object
        array = np.zeros((properties['size'][0], properties['size'][1], 4), dtype=np.uint8)
        array[:, :] = properties['color']
        img = Image.fromarray(array, properties['mode'])
    
    # Save the image to a file with a format that supports all color models
    file_path = f'./tmp/{model_name.lower()}_image.jpg'
    img.save(file_path)

print("Images generated and saved to ./tmp/ directory.")