import os

# Create a directory to save the generated mp4 files
os.makedirs('./tmp/', exist_ok=True)

# Generate an example mp4 file with DRM protection
mp4_file_path = './tmp/example.mp4'
with open(mp4_file_path, 'w') as f:
    f.write('MP4 file with DRM protection')

print(f'Generated MP4 file with DRM protection at: {mp4_file_path}')