import os

# Create a directory to store the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate pixdata files with more complex file structures
features_list = [
    {
        'Resolution': '1920x1080',
        'Color Depth': '24-bit'
    },
    {
        'Resolution': '3840x2160',
        'Color Depth': '32-bit',
        'Refresh Rate': '60Hz'
    },
    {
        'Resolution': '1280x720',
        'Color Depth': '16-bit',
        'HDR Support': 'Yes'
    }
]

for i, features in enumerate(features_list):
    filename = f'./tmp/pixdata_{i}.txt'
    with open(filename, 'w') as file:
        file.write('Features:\n')
        for feature, value in features.items():
            if isinstance(value, dict):
                file.write(f'{feature}:\n')
                for sub_feature, sub_value in value.items():
                    file.write(f'\t{sub_feature}: {sub_value}\n')
            else:
                file.write(f'{feature}: {value}\n')

print('Generated pixdata files with complex file structures successfully.')