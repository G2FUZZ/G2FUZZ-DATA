import os

# Create a directory to store the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate pixdata files with additional complex features
features = [
    {
        'Resolution': '1920x1080',
        'Format': 'JPEG',
        'Size': '2MB'
    },
    {
        'Resolution': '1280x720',
        'Format': 'PNG',
        'Size': '1.5MB'
    },
    {
        'Resolution': '3840x2160',
        'Format': 'TIFF',
        'Size': '4MB'
    }
]

for i, feature_set in enumerate(features):
    filename = f'./tmp/pixdata_{i}.txt'
    with open(filename, 'w') as file:
        file.write('Features:\n')
        for feature, value in feature_set.items():
            file.write(f'{feature}: {value}\n')

print('Generated pixdata files with complex features successfully.')