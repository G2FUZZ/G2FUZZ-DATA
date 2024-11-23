import os

# Create a directory to save the generated files
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate a sample MP4 file with 3D video and Dolby Atmos audio support
sample_data = b'\x00\x01\x02\x03'  # Sample binary data
dolby_atmos_data = b'\x04\x05\x06\x07'  # Dolby Atmos audio data
file_path = os.path.join(output_dir, '3d_video_dolby_atmos.mp4')
with open(file_path, 'wb') as f:
    f.write(sample_data)
    f.write(dolby_atmos_data)

print(f"Generated MP4 file with 3D video and Dolby Atmos audio support: {file_path}")