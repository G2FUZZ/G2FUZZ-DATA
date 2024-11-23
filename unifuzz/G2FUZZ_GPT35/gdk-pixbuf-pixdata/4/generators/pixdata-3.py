import os

# Create a directory to store the generated files
os.makedirs('./tmp', exist_ok=True)

# Define the features
features = {
    'Color depth': '8-bit'
}

# Generate and save the 'pixdata' files
for i in range(5):
    with open(f'./tmp/pixdata_{i}.txt', 'w') as file:
        for feature, value in features.items():
            file.write(f'{feature}: {value}\n')