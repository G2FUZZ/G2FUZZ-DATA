import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with the specified feature
for i in range(3):
    filename = f'./tmp/file_{i}.flv'
    with open(filename, 'wb') as file:
        file.write(b'FLV File - Quality: FLV files can maintain good quality while keeping file sizes relatively small.')

print('FLV files generated successfully.')