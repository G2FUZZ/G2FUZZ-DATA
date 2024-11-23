import os

# Create a directory to store the generated mp4 files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp4 file with DRM protection and Dolby Atmos audio support
sample_data = b"This is a sample DRM protected mp4 file with Dolby Atmos audio support."
file_path = './tmp/sample_drm_dolby_atmos_protected.mp4'

with open(file_path, 'wb') as file:
    file.write(sample_data)

print(f"Generated DRM protected mp4 file with Dolby Atmos audio support at: {file_path}")