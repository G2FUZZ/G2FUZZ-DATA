# Example: Writing to a file in ./tmp/ directory

# Define the path to the file
file_path = './tmp/example_file.txt'

# Ensure the directory exists (Python 3.5+)
import os
os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Corrected the typo here

# Write data to the file
with open(file_path, 'w') as file:
    file.write('Hello, this is a test file.')

print(f'File has been saved to {file_path}')