import os

# Define the directory path where the file will be saved
directory_path = './tmp'

# Ensure the directory exists. If not, create it.
if not os.path.exists(directory_path):
    os.makedirs(directory_path)

# Define the full path for the new file within the specified directory
file_path = os.path.join(directory_path, 'generated_file.txt')

# Write some content to the file
try:
    with open(file_path, 'w') as file:
        file.write("This is a test file saved in ./tmp/")
    print(f"File successfully saved to {file_path}")
except IOError as e:
    print(f"An error occurred while writing the file: {e}")