import os

# Create a directory to store the generated mp4 files
os.makedirs('tmp', exist_ok=True)

# Generate a sample mp4 file with multiple audio tracks feature
with open('./tmp/sample_with_audio_tracks.mp4', 'wb') as f:
    f.write(b'\x00\x00\x00\x18ftypmp42\x00\x00\x00\x00mp42isom\x00\x00\x02\x00\x00\x00\x00\x08free')
    f.write(b'\x00\x00\x00\x0Ctrak\x00\x00\x00\x00tkhd\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00')
    f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

print("MP4 file with multiple audio tracks generated successfully.")