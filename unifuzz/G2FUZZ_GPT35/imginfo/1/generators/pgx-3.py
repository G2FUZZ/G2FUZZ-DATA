import os

# Define the features to be included in the 'pgx' files
features = """
1. Format: pgx
2. Author: AI Assistant
3. Compression: 'pgx' files might utilize compression techniques to reduce file size, such as lossless or lossy compression algorithms.
"""

# Create a directory to store the 'pgx' files if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate 'pgx' files containing the specified features
for i in range(3):  # Create 3 'pgx' files
    filename = f'{directory}file_{i + 1}.pgx'
    with open(filename, 'w') as file:
        file.write(features)

print(f"Generated 3 'pgx' files in the './tmp/' directory.")