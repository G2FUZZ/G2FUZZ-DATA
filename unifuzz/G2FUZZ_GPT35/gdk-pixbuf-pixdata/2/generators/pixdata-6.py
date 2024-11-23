import os

# Create a directory to save the pixdata files
os.makedirs('./tmp/', exist_ok=True)

# Generate the pixdata files
features = {
    'Palette': {
        'description': 'For indexed color images, a palette may be included to map pixel values to specific colors.'
    }
}

for feature_name, feature_info in features.items():
    with open(f'./tmp/{feature_name.lower()}.txt', 'w') as f:
        f.write(f"Feature: {feature_name}\n\nDescription: {feature_info['description']}\n")