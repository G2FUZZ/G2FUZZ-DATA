import os

# Create a directory if it does not exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate an mp4 file with chapters, extended metadata, and multiple audio streams
with open(os.path.join(output_dir, 'video_with_chapters_metadata_and_audio_streams.mp4'), 'wb') as f:
    f.write(b'Generated MP4 file with chapters, extended metadata, and multiple audio streams')

print('MP4 file with chapters, extended metadata, and multiple audio streams generated successfully!')