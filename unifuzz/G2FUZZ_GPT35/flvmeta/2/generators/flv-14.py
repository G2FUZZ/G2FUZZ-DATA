import os

# Create a directory to store the generated FLV files if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with small file sizes and Alpha Channel feature
file_sizes = [100, 200, 150, 180, 120]  # in KB

for idx, size in enumerate(file_sizes):
    with open(f'./tmp/video_{idx}.flv', 'wb') as f:
        # Write dummy data to create a file with the specified size

        # Write FLV header
        f.write(b'FLV\x01\x05\0\0\0\x09\0\0\0\0')

        # Write previous tags (if any)
        f.write(b'\0\0\0\x0c\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0')

        # Write Video Tag
        f.write(b'\x09\0\0\0\x10\0\0\0\0\0\0\0\0')

        # Write Audio Tag
        f.write(b'\x08\0\0\0\x10\0\0\0\0\0\0\0\0')
        
        # Write Alpha Channel Tag
        f.write(b'\x08\0\0\0\x10\0\0\0\0\0\0\0\0')  # Dummy data for Alpha Channel

        # Write end of FLV tag
        f.write(b'\0\0\0\x09\0\0\0\0\0\0\0\0')

print("FLV files with small file sizes and Alpha Channel feature have been generated and saved in the './tmp/' directory.")