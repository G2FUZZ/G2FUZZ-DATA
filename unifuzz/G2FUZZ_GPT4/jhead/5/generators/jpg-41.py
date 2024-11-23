import os

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Define the file path
file_path = './tmp/sample_file.txt'

# Write a message to the file
with open(file_path, 'w') as file:
    file.write('Hello, world!')

print(f'File has been saved to {file_path}')