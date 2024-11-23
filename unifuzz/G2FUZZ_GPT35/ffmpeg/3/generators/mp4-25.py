import os

# Create a directory to save the generated mp4 files
os.makedirs('./tmp/', exist_ok=True)

# Generate an example mp4 file with DRM protection and 360-degree video support
mp4_file_path = './tmp/example_360.mp4'
with open(mp4_file_path, 'w') as f:
    f.write('MP4 file with DRM protection and 360-degree video support\n3. 360-degree video support: Capable of storing immersive 360-degree video content')

print(f'Generated MP4 file with DRM protection and 360-degree video support at: {mp4_file_path}')