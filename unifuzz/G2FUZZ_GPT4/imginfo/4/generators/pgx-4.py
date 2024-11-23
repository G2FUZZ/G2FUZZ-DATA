import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the content to be saved
content = """4. **Simplicity and Ease of Use**: Due to its straightforward structure, PGX files are relatively simple to create, read, and write by software, making them an excellent choice for software developers and researchers working on image processing projects that require direct access to pixel data without dealing with compression artifacts."""

# Define the file path
file_path = './tmp/example.pgx'

# Write the content to the file
with open(file_path, 'w') as file:
    file.write(content)

print(f'File saved to {file_path}')