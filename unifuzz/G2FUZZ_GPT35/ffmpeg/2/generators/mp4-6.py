import os

# Create a directory to store the generated mp4 files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp4 file with DRM protection
sample_data = b"This is a sample DRM protected mp4 file."
file_path = './tmp/sample_drm_protected.mp4'

with open(file_path, 'wb') as file:
    file.write(sample_data)

print(f"Generated DRM protected mp4 file at: {file_path}")