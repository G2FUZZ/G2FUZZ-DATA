import os
import json

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define a function to generate layer data
def generate_layer_data(layers=3, width=100, height=100):
    """
    Generate a simple representation of layer data for an image.
    Each layer contains random RGB pixel values.

    :param layers: Number of layers to generate
    :param width: Width of the image
    :param height: Height of the image
    :return: A list of layer data
    """
    import random
    layer_data = []
    for _ in range(layers):
        layer = {'pixels': []}
        for _ in range(height):
            row = []
            for _ in range(width):
                # Generate a random RGB pixel
                pixel = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                row.append(pixel)
            layer['pixels'].append(row)
        layer_data.append(layer)
    return layer_data

# Generate layer data
layers = generate_layer_data(layers=5, width=50, height=50)

# Save the generated data to a file in the ./tmp/ directory
file_path = './tmp/pixdata_layers.json'
with open(file_path, 'w') as file:
    json.dump(layers, file)

print(f"Layer data saved to {file_path}")