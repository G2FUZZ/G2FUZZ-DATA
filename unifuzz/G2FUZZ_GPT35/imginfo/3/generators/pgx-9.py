import os

# Create a directory to store the generated 'pgx' files
os.makedirs('./tmp/', exist_ok=True)

# Define the content for the 'pgx' files
content = """
9. Versioning: Different versions of the Progenex software may support different features or extensions of the 'pgx' file format.
"""

# Generate 'pgx' files with the specified content
for i in range(1, 4):  # Generate 3 'pgx' files
    file_name = f'./tmp/file_{i}.pgx'
    with open(file_name, 'w') as file:
        file.write(content)

print("Generated 'pgx' files successfully.")