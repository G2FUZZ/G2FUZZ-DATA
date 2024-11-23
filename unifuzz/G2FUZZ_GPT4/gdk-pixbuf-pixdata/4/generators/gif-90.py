import os

# Ensure the ./tmp/ directory exists
directory = "./tmp"
if not os.path.exists(directory):
    os.makedirs(directory)

# Path to the file to be saved in ./tmp/
file_path = os.path.join(directory, "example_file.txt")

# Writing data to the file
with open(file_path, 'w') as file:
    file.write("This is an example of saving a file into ./tmp/ directory.")

print(f"File saved successfully in {file_path}")