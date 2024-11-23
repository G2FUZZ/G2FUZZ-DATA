import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# The path to the file where you want to save the content
file_path = './tmp/generated_file.txt'

# The content you want to write to the file
content = "This is some generated content."

# Writing the content to the file
with open(file_path, 'w') as file:
    file.write(content)

print(f"File has been saved to {file_path}")