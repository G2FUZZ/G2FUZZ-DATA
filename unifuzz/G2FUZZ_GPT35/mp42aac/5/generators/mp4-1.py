import os

# Create a directory to store the generated mp4 files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp4 file (empty file for demonstration purposes)
file_path = './tmp/sample.mp4'
with open(file_path, 'wb') as f:
    f.write(b'')

print(f"Generated MP4 file: {file_path}")