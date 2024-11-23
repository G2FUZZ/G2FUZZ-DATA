import os

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with small file size
for i in range(5):
    with open(f'./tmp/video_{i}.flv', 'wb') as file:
        # Write some data to represent the FLV file
        file.write(b'FLV File Data')

print("FLV files generated successfully in the ./tmp/ directory.")