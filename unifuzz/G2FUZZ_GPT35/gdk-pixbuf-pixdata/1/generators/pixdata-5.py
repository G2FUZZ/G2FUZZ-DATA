import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate 'pixdata' files with the specified features
features = {
    'Compression': 'Information about any compression techniques used to store the image data.'
}

for feature_name, feature_description in features.items():
    file_name = os.path.join(directory, f'{feature_name.lower()}.pixdata')
    with open(file_name, 'w') as file:
        file.write(feature_description)

    print(f"Generated '{file_name}' containing '{feature_name}': {feature_description}")