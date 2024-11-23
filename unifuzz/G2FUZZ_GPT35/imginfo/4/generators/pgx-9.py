import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate pgx files with the given features
features = "9. Compatibility: 'pgx' files may have limitations in terms of software compatibility, as they are specific to the PGX software."
for i in range(3):
    with open(f'./tmp/file_{i}.pgx', 'w') as file:
        file.write(features)

print("pgx files generated and saved in ./tmp/")