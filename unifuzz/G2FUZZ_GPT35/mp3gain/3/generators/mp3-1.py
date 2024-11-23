import os

# Create a directory to save the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Simulate generating an mp3 file with lossy compression feature
filename = './tmp/lossy_compression_example.mp3'
with open(filename, 'w') as file:
    file.write('This is a sample mp3 file with lossy compression feature.')

print(f'Generated mp3 file with lossy compression feature saved as: {filename}')