import os

# Create a directory to save the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with scripting support
for i in range(5):
    filename = f'./tmp/file_{i}.flv'
    with open(filename, 'wb') as file:
        file.write(b'FLV File with ActionScript Support')
        print(f'Generated {filename}')