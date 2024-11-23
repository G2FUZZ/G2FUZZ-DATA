# Define the directory and file name
directory = './tmp/'
file_name = 'example.txt'
file_path = directory + file_name

# Ensure the directory exists (create it if it doesn't)
import os
if not os.path.exists(directory):
    os.makedirs(directory)

# Write text to the file
with open(file_path, 'w') as file:
    file.write('Hello, world!')

print(f'File saved to {file_path}')