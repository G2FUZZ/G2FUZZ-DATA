import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate pixdata files with the given feature
features = {
    'Compression ratio': 0.75
}

for feature, value in features.items():
    with open(f'./tmp/{feature.lower().replace(" ", "_")}.pixdata', 'w') as file:
        file.write(f'{feature}: {value}')