import os

# Create a directory to save the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate an empty mp3 file
file_path = './tmp/generated_file.mp3'
open(file_path, 'w').close()

print(f"Generated mp3 file with file extension: {file_path}")