import os

# Ensure tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Generate pgx files with encryption feature
for i in range(3):
    filename = f'./tmp/file_{i + 1}.pgx'
    with open(filename, 'w') as file:
        file.write("Encryption: 'pgx' files could be encrypted to secure the contained data.")

print("pgx files generated and saved in ./tmp folder.")