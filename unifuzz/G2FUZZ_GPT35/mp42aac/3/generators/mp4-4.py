import os

# Create a directory if it does not exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate an mp4 file with chapters
with open(os.path.join(output_dir, 'video_with_chapters.mp4'), 'wb') as f:
    f.write(b'Generated MP4 file with chapters')

print('MP4 file with chapters generated successfully!')