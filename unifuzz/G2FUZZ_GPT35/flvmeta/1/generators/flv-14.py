import os

# Create a directory to save the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with scripting support and Chapter markers
for i in range(6):
    filename = f'./tmp/file_{i}.flv'
    with open(filename, 'wb') as file:
        file.write(b'FLV File with ActionScript Support and Chapter markers')
        print(f'Generated {filename}')