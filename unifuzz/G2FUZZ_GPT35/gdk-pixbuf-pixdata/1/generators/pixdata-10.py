import os

# Define the features to be included in the 'pixdata' file
features = {
    'Software-specific data': 'Additional features specific to the software that created the pixdata file.'
}

# Create a directory if it does not exist
directory = './tmp'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate the 'pixdata' files with the specified features
for feature_name, feature_description in features.items():
    file_path = os.path.join(directory, f'{feature_name.lower().replace(" ", "_")}.txt')
    with open(file_path, 'w') as file:
        file.write(f'{feature_name}: {feature_description}')

print('pixdata files generated and saved in ./tmp/ successfully.')