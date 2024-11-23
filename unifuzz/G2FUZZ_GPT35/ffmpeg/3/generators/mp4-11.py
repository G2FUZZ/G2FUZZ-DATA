import os

# Create a directory to store the generated mp4 files
os.makedirs('tmp', exist_ok=True)

# Generate a sample mp4 file with Closed captioning support feature
with open('./tmp/sample_closed_captioning.mp4', 'wb') as f:
    f.write(b'\x00\x00\x00\x18ftypmp42\x00\x00\x00\x00mp42isom\x00\x00\x02\x00\x00\x00\x00\x08free\x00\x00\x00\x1cttxt\x00\x00\x00\x01\x00\x00\x00\x00')

print("MP4 file with Closed captioning support generated successfully.")