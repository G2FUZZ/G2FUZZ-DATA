# Ensure the directory exists
import os

# Create the directory './tmp/' if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Path to the file to be saved
file_path = './tmp/my_file.txt'

# Data to be written to the file
data = "This is the data to be saved in the file."

# Writing data to the file
with open(file_path, 'w') as file:
    file.write(data)

print(f"File has been saved to {file_path}")