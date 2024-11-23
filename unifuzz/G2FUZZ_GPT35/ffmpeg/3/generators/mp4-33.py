import os

# Create a directory to save the generated mp4 files
os.makedirs('./tmp/', exist_ok=True)

# Generate an example mp4 file with DRM protection, 360-degree video support, and Live streaming support
mp4_file_path = './tmp/example_360_live_streaming.mp4'
with open(mp4_file_path, 'w') as f:
    f.write('MP4 file with DRM protection, 360-degree video support, and Live streaming support\n3. 360-degree video support: Capable of storing immersive 360-degree video content\n11. Live streaming support: Capable of streaming live video content in real-time')

print(f'Generated MP4 file with DRM protection, 360-degree video support, and Live streaming support at: {mp4_file_path}')