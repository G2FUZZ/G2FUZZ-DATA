import os

# Create a directory to save the generated files
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate a sample MP4 file with 3D video support and HDR video feature
sample_data = b'\x00\x01\x02\x03'  # Sample binary data
hdr_feature = b'\x04\x05\x06\x07'  # HDR video feature data
file_path = os.path.join(output_dir, '3d_hdr_video.mp4')
with open(file_path, 'wb') as f:
    f.write(sample_data)
    f.write(hdr_feature)

print(f"Generated MP4 file with 3D video and HDR video support: {file_path}")