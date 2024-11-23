import os

# Create a directory if it does not exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate 'pgx' files with genetic data and metadata
file_contents = """
# Example 'pgx' file
## Genetic Data
DNA Sequence: ATCGATCGATCG
Gene Expressions: [0.5, 0.3, 0.7, 0.9]

## Metadata
Sample ID: 12345
Experiment Date: 2022-01-01
"""

file_names = ['file1.pgx', 'file2.pgx']

for file_name in file_names:
    with open(os.path.join(directory, file_name), 'w') as file:
        file.write(file_contents)

print(f'Files saved in {directory}')