import os

# Create a directory if not exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample FLV file with the given features
file_path = './tmp/sample.flv'
with open(file_path, 'wb') as file:
    file.write(b'FLV file with good video and audio quality and small file size.')

print(f'FLV file generated successfully at: {file_path}')