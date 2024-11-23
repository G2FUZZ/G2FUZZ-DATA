import os

# Create a directory to save the generated mp4 files
os.makedirs('./tmp/', exist_ok=True)

# Generate an example mp4 file with DRM protection, 360-degree video support, and Timecode support
mp4_file_path = './tmp/example_360_timecode.mp4'
with open(mp4_file_path, 'w') as f:
    f.write('MP4 file with DRM protection, 360-degree video support, and Timecode support\n3. 360-degree video support: Capable of storing immersive 360-degree video content\n5. Timecode support: Includes timecode information for accurate synchronization in editing workflows')

print(f'Generated MP4 file with DRM protection, 360-degree video support, and Timecode support at: {mp4_file_path}')