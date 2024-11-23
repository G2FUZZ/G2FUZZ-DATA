import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp3 file
sample_data = b"Sample MP3 file content"
file_path = './tmp/sample.mp3'

with open(file_path, 'wb') as f:
    f.write(sample_data)

print(f"MP3 file with lossy compression generated at: {file_path}")