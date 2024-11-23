import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate the pixdata files
features = {
    'Color space': 'RGB'
}

for i in range(5):
    with open(f'./tmp/pixdata_{i}.txt', 'w') as file:
        for feature, value in features.items():
            file.write(f'{feature}: {value}\n')

print('pixdata files generated successfully.')