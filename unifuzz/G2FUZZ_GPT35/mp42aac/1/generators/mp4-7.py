import os

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp4 file with DRM protection and Text track support
sample_data = b'Fake MP4 data with DRM protection and Text track support'
file_path = './tmp/sample_drm_text_track.mp4'

with open(file_path, 'wb') as file:
    file.write(sample_data)

print(f"Generated MP4 file with DRM protection and Text track support: {file_path}")