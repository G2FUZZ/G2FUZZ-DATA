import os

# Create a directory to store the 'ras' files
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate 'ras' files with the specified features
features = "10. Conversion: 'ras' files may need to be converted to more widely supported formats for easier sharing and viewing."

num_files = 3
for i in range(num_files):
    filename = f'{directory}file_{i + 1}.ras'
    with open(filename, 'w') as file:
        file.write(features)

print(f"{num_files} 'ras' files have been generated and saved in the '{directory}' directory.")