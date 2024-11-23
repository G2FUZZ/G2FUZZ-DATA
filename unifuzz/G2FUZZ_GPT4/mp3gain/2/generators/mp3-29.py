import os

# Ensure the ./tmp/ directory exists
directory = "./tmp/"
if not os.path.exists(directory):
    os.makedirs(directory)

# Specify the filename
filename = "example.txt"

# Combine the directory and filename to create the path
file_path = os.path.join(directory, filename)

# Write a message to the file
with open(file_path, 'w') as file:
    file.write("Hello, this is a test file saved in ./tmp/")

print(f"File saved to {file_path}")