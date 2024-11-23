import os

# Create a directory to store the generated mp4 files
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate a sample mp4 file with DRM protection
sample_file_path = os.path.join(output_dir, 'sample_drm_protected.mp4')
with open(sample_file_path, 'wb') as f:
    f.write(b'Generated DRM protected MP4 file content')

print(f"Generated DRM protected MP4 file: {sample_file_path}")