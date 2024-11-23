import os

# Define the features
features = {
    'Compression type': 'JPEG'
}

# Create the directory if it doesn't exist
directory = './tmp/'
os.makedirs(directory, exist_ok=True)

# Save the features into a file
file_path = os.path.join(directory, 'pixdata.txt')
with open(file_path, 'w') as file:
    for key, value in features.items():
        file.write(f'{key}: {value}\n')

print(f'Features saved into {file_path}')