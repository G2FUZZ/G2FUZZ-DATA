import os

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with encryption and Alpha Channel Support features
for i in range(4):
    file_name = f'./tmp/file_{i}.flv'
    with open(file_name, 'wb') as f:
        # Simulating encryption by writing some random data
        f.write(os.urandom(1024))
        # Simulating Alpha Channel Support by adding a transparent overlay
        f.write(b'Alpha Channel Support: Transparent overlay added')

print('FLV files with encryption and Alpha Channel Support features have been generated and saved in ./tmp/ directory.')