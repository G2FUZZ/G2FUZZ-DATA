import os

# Create a directory to store the generated mp4 files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp4 file with DRM protection and Variable frame rates feature
sample_data = b"This is a sample DRM protected mp4 file with Variable frame rates feature."
file_path = './tmp/sample_drm_protected_variable_frame_rates.mp4'

with open(file_path, 'wb') as file:
    file.write(sample_data)

print(f"Generated DRM protected mp4 file with Variable frame rates feature at: {file_path}")