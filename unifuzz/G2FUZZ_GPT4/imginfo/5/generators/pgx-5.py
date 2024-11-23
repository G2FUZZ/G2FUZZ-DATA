import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the path for the new PGX file
file_path = './tmp/example.pgx'

# PGX file content - simple structure example
# Note: In a real scenario, this would be image data. Here, it's just simple text for demonstration.
pgx_content = """
PGX file format example
Width: 100
Height: 100
Depth: 8
Data:
...binary or textual data...
"""

# Writing the content to the PGX file
with open(file_path, 'w') as file:
    file.write(pgx_content)

print(f'PGX file created at: {file_path}')