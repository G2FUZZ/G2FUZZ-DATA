import os

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Define the path for the file to be saved in ./tmp/
file_path = './tmp/my_file.txt'

# Data to be written to the file
data = "This is some data I want to save to a file."

# Writing the data to the file
with open(file_path, 'w') as file:
    file.write(data)

print("File saved successfully.")