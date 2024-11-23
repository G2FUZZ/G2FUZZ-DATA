import os

# Create a directory to store the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate pixdata files with the specified features
features = {
    'Resolution': '1920x1080'
}

for i in range(3):
    filename = f'./tmp/pixdata_{i}.txt'
    with open(filename, 'w') as file:
        file.write('Features:\n')
        for feature, value in features.items():
            file.write(f'{feature}: {value}\n')

print('Generated pixdata files successfully.')