import os

# Define the directory and file path
dir_path = './tmp/'
file_path = os.path.join(dir_path, 'example_file.txt')

# Ensure the directory exists
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
    print(f"Directory {dir_path} created")

# Data to be written to the file
data = "Hello, world!"

# Write data to the file
with open(file_path, 'w') as file:
    file.write(data)

print(f"File has been successfully created and saved to {file_path}")