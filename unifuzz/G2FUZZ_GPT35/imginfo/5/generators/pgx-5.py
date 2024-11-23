import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate pgx files with layers feature
for i in range(3):
    file_name = f'./tmp/file_{i}.pgx'
    with open(file_name, 'w') as file:
        file.write(f'Layers feature supported in {file_name}\n')