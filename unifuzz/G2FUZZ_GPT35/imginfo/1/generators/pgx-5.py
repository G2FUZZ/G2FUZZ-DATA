import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample 'pgx' file with transparency information
file_path = './tmp/sample.pgx'
with open(file_path, 'w') as file:
    file.write("Transparency: 'pgx' files may support transparency information, like alpha channels or transparency masks.")

print(f"File '{file_path}' created successfully.")