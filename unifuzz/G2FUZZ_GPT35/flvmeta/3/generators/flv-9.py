import os

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with encryption feature
for i in range(3):
    file_name = f'./tmp/file_{i}.flv'
    with open(file_name, 'wb') as f:
        # Simulating encryption by writing some random data
        f.write(os.urandom(1024))

print('FLV files with encryption feature have been generated and saved in ./tmp/ directory.')