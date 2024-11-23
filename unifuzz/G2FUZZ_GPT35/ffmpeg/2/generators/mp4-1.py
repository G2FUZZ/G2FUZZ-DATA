import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample MP4 file (empty file for demonstration purposes)
file_path = './tmp/sample.mp4'
with open(file_path, 'wb') as f:
    f.write(b'')

print(f"MP4 file '{file_path}' has been generated successfully.")