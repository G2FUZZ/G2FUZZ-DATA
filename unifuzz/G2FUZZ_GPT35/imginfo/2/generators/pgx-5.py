import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate pgx files with encryption feature
num_files = 5
for i in range(num_files):
    file_name = f'./tmp/file_{i+1}.pgx'
    with open(file_name, 'w') as file:
        file.write("Encryption: Some 'pgx' files can be encrypted to secure the image data from unauthorized access.")