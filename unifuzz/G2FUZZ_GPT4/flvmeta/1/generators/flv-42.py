import os

# Ensure the ./tmp/ directory exists
directory = "./tmp/"
if not os.path.exists(directory):
    os.makedirs(directory)

# Define the path to the file within the ./tmp/ directory
file_path = os.path.join(directory, "example_file.txt")

# Data to be written to the file
data = "Hello, this is a test file."

# Writing data to the file
with open(file_path, 'w') as file:
    file.write(data)

print(f"File has been successfully written to {file_path}")