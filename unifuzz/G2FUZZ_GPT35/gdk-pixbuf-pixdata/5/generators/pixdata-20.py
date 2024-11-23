import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate the pixdata files
features = {
    'Rendering instructions': 'Instructions on how to render or display the image data.'
}

for feature, description in features.items():
    with open(f'./tmp/{feature.lower().replace(" ", "_")}.pixdata', 'w') as file:
        file.write(f'{feature}:\n{description}')