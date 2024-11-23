import os

# Create a directory if it does not exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate pixdata files
features = {
    'Compression': 'Techniques used to reduce file size, such as lossless or lossy compression.'
}

for feature, description in features.items():
    with open(f'./tmp/{feature.lower()}.pixdata', 'w') as file:
        file.write(f'Feature: {feature}\nDescription: {description}')

print('pixdata files generated successfully!')