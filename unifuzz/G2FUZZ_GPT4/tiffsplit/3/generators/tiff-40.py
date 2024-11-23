# Ensure the ./tmp/ directory exists
import os

# Create the directory if it does not exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# The path to the file where you want to save the content
file_path = './tmp/example_file.txt'

# The content you want to write to the file
content = "This is some example content."

# Writing the content to the file
with open(file_path, 'w') as file:
    file.write(content)

print("File saved successfully in ./tmp/")