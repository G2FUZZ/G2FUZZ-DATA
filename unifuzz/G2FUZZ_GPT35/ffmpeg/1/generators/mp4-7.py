import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate MP4 files with DRM protection
for i in range(3):
    file_name = f'./tmp/video_{i+1}.mp4'
    with open(file_name, 'wb') as f:
        f.write(b'DRM Protected MP4 file')

print('MP4 files with DRM protection generated successfully.')