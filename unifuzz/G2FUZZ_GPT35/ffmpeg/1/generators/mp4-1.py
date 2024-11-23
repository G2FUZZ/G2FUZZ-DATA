import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate an empty mp4 file
file_path = './tmp/generated_file.mp4'
with open(file_path, 'w') as f:
    pass

print(f"Generated mp4 file: {file_path}")