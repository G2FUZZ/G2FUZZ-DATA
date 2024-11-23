import os

# Create a directory if it does not exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate 'ras' files with the provided features
features = "Multiple image support: Some 'ras' formats may allow storing multiple images within a single file, such as image sequences or layers."

for i in range(2):  # Generate 2 'ras' files
    file_name = f'{directory}file_{i}.ras'
    with open(file_name, 'w') as file:
        file.write(features)

print("Files generated successfully in ./tmp/ directory.")