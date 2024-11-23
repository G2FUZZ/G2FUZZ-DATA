import os

# Create a directory to save the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with scripting support and Scalability feature
for i in range(6):
    filename = f'./tmp/file_{i}.flv'
    with open(filename, 'wb') as file:
        if i == 5:
            file.write(b'FLV File with ActionScript Support and Scalability Feature')
            print(f'Generated {filename} with Scalability Feature')
        else:
            file.write(b'FLV File with ActionScript Support')
            print(f'Generated {filename}')