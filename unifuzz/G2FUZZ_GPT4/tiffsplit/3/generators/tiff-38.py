# Example: Writing a text file to ./tmp/ directory

# Import the os module to work with the operating system
import os

# Define the directory path
dir_path = './tmp/'

# Check if the directory exists
if not os.path.exists(dir_path):
    # If the directory does not exist, create it
    os.makedirs(dir_path)

# Define the file path
file_path = os.path.join(dir_path, 'example.txt')

# Write a file to the specified directory
with open(file_path, 'w') as file:
    file.write('Hello, this is a test file.')

print(f'File has been saved to {file_path}')