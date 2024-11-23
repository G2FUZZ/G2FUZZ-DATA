# Define the directory and file name
directory = './tmp/'
file_name = 'example.txt'
file_path = directory + file_name

# Ensure the directory exists
import os
if not os.path.exists(directory):
    os.makedirs(directory)

# Write text to the file
with open(file_path, 'w') as file:
    file.write('This is an example text.')

print(f'File saved to {file_path}')