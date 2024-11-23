import os

# Define the directory path
dir_path = './tmp/'

# Check if the directory exists, and create it if it doesn't
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

# Define the file path
file_path = os.path.join(dir_path, 'example.txt')

# Write text to the file
with open(file_path, 'w') as file:
    file.write('Hello, world!')

print(f'File saved to {file_path}')