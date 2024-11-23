import os

# Define the features to be included in the 'pgx' files
features = "Compatibility: 'pgx' files are compatible with the Progenex software for analysis and visualization of genetic data."

# Create the directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate 'pgx' files with the specified features
for i in range(3):
    filename = f'./tmp/file_{i + 1}.pgx'
    with open(filename, 'w') as file:
        file.write(features)

print("Files generated successfully!")