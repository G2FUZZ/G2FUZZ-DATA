import os

# Create a directory if it does not exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Define the features
features = {
    'Metadata': {
        'creation_date': '2022-09-15',
        'author': 'John Doe',
        'tags': ['nature', 'landscape', 'mountains']
    }
}

# Save the features to a file
for feature_name, data in features.items():
    file_path = f'./tmp/{feature_name.lower()}.pixdata'
    with open(file_path, 'w') as file:
        file.write(f'Feature: {feature_name}\n')
        for key, value in data.items():
            if isinstance(value, list):
                value_str = ', '.join(value)
            else:
                value_str = str(value)
            file.write(f'{key}: {value_str}\n')

print('Files saved successfully.')