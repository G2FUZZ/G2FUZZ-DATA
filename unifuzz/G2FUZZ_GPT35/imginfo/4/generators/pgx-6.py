import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate pgx files with transparency feature
for i in range(3):
    file_name = f'./tmp/file_{i}.pgx'
    with open(file_name, 'w') as file:
        file.write('Transparency Feature: Alpha Channels and Transparent Backgrounds\n')
    print(f'Generated {file_name}')