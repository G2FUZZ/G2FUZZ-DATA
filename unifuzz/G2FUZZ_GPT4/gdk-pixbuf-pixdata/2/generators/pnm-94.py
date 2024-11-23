# Ensure the ./tmp/ directory exists
import os

# Create the directory if it doesn't exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# The path to the file where you want to save the content
file_path = './tmp/example_file.txt'

# The content you want to write to the file
content = "This is an example of saving a file."

# Writing the content to the file
with open(file_path, 'w') as file:
    file.write(content)

print(f"File has been saved to {file_path}")