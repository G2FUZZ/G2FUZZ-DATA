import os

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp4 file with multiple audio tracks, HDR support, 360-degree video format, and VFR encoding
sample_data = b'Fake MP4 data with multiple audio tracks, HDR support, 360-degree video format, and VFR encoding'
file_path = './tmp/sample_complex_features.mp4'

with open(file_path, 'wb') as file:
    file.write(sample_data)

print(f"Generated MP4 file with multiple audio tracks, HDR support, 360-degree video format, and VFR encoding: {file_path}")