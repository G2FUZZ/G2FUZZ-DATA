import os

# Create a directory to store the generated FLV files if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with small file sizes
file_sizes = [100, 200, 150, 180, 120]  # in KB

for idx, size in enumerate(file_sizes):
    with open(f'./tmp/video_{idx}.flv', 'wb') as f:
        # Write dummy data to create a file with the specified size
        f.write(b'\0' * size * 1024)

print("FLV files with small file sizes have been generated and saved in the './tmp/' directory.")