import os

# Create a directory if it does not exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate a sample MP4 file with DRM feature
file_path = os.path.join(directory, 'sample.mp4')
with open(file_path, 'wb') as file:
    file.write(b'Generated MP4 file with DRM feature')

print(f'MP4 file with DRM feature generated at: {file_path}')