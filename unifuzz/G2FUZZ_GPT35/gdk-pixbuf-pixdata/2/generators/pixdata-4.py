import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate pixdata files with the specified features
features = {
    'Color space': 'RGB'
}

for i in range(3):
    filename = f'{directory}pixdata_{i}.txt'
    with open(filename, 'w') as file:
        for key, value in features.items():
            file.write(f'{key}: {value}\n')

print('pixdata files have been generated and saved in the tmp directory.')