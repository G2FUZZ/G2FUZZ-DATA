import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate 'ras' files with the specified feature
file_content = "8. Lossless vs. lossy compression: 'ras' files may support both lossless and lossy compression methods, depending on the specific implementation."

for i in range(3):  # Generate 3 'ras' files
    file_name = f'{directory}file_{i + 1}.ras'
    with open(file_name, 'w') as file:
        file.write(file_content)

print("Files generated successfully.")