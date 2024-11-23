import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp3 file with VBR support
sample_file_path = './tmp/sample.mp3'

# Simulating the generation of an mp3 file with VBR support
with open(sample_file_path, 'w') as f:
    f.write('Sample mp3 file with VBR support')

print(f'MP3 file with VBR support generated and saved at: {sample_file_path}')