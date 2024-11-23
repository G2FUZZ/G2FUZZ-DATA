import os

# Create a directory to store the generated files
directory = './tmp/'
os.makedirs(directory, exist_ok=True)

# Generate 'ras' files with sample features
for i in range(3):
    file_name = f'file_{i}.ras'
    with open(os.path.join(directory, file_name), 'w') as file:
        file.write(f"File {i} content:\n")
        file.write("File structure: The file structure of 'ras' files can vary, including header information, image data blocks, color palette information (if applicable), and other sections.\n")
    print(f"Generated {file_name} in {directory}")