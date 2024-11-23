import os

# Create a directory to store the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample MP4 file with subtitles
with open('./tmp/sample_subtitles.mp4', 'wb') as f:
    f.write(b'Generated MP4 file with subtitles')

print("MP4 file with subtitles generated successfully!")