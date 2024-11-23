import os

# Create a directory to save the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with ActionScript code
for i in range(3):
    file_name = f'./tmp/file_{i}.flv'
    with open(file_name, 'wb') as file:
        file.write(b'FLV Header\n')
        file.write(b'FLV Body\n')
        file.write(b'ActionScript code for interactive features\n')
    print(f'Generated {file_name}')

print('FLV files with ActionScript code have been generated and saved in ./tmp/')