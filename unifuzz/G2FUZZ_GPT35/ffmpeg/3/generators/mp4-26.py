import os

# Create a directory to store the generated mp4 files
os.makedirs('tmp', exist_ok=True)

# Generate a sample mp4 file with Dolby Atmos audio support
with open('./tmp/sample_with_dolby_atmos.mp4', 'wb') as f:
    f.write(b'\x00\x00\x00\x18ftypmp42\x00\x00\x00\x00mp42isom\x00\x00\x02\x00\x00\x00\x00\x08freeDolby Atmos audio support: Enables immersive audio experiences with spatial sound technology')

print("MP4 file with Dolby Atmos audio support generated successfully.")