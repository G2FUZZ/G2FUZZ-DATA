import os
import json
import random

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def generate_random_pixels(width, height):
    """
    Generates random pixel data for an image of the given dimensions.
    """
    pixels = []
    for y in range(height):
        for x in range(width):
            pixels.append({
                "x": x, "y": y,
                "r": random.randint(0, 255),
                "g": random.randint(0, 255),
                "b": random.randint(0, 255)
            })
    return pixels

def create_image_info(width, height, color_depth="8-bit", color_model="RGB"):
    """
    Creates a dictionary containing image info.
    """
    return {
        "width": width,
        "height": height,
        "color_depth": color_depth,
        "color_model": color_model  # Corrected from colorModel to color_model
    }

# Generate pixdata for multiple images
pixdata_features = {
    "metadata": {
        "creator": "Python Script",
        "description": "Extended pixdata file containing multiple images with layers and random pixel data.",
        "version": 2.0
    },
    "images": [
        {
            "image_id": 1,
            "image_info": create_image_info(100, 100),
            "layers": [
                {
                    "layer_id": 1,
                    "layer_description": "Background layer",
                    "pixels": generate_random_pixels(100, 100)
                },
                {
                    "layer_id": 2,
                    "layer_description": "Foreground layer",
                    "pixels": generate_random_pixels(100, 100)
                }
            ]
        },
        {
            "image_id": 2,
            "image_info": create_image_info(200, 150, color_depth="16-bit", color_model="RGBA"),
            "layers": [
                {
                    "layer_id": 1,
                    "layer_description": "Single layer",
                    "pixels": generate_random_pixels(200, 150)
                }
            ]
        }
    ]
}

# Saving the extended pixdata to a file
file_path = './tmp/extended_sample_pixdata.json'  # Saving as a JSON for demonstration purposes
with open(file_path, 'w') as file:
    json.dump(pixdata_features, file, indent=4)

print(f"Extended sample pixdata file saved to {file_path}")