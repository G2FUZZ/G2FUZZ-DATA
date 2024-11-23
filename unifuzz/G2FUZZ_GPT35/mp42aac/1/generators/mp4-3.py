import os

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp4 file with DRM protection
sample_data = b'Fake MP4 data with DRM protection'
file_path = './tmp/sample_drm_protected.mp4'

with open(file_path, 'wb') as file:
    file.write(sample_data)

print(f"Generated DRM-protected MP4 file: {file_path}")