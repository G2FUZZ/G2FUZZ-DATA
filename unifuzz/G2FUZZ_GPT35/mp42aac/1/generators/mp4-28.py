import os

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp4 file with multiple tracks, chapters, and metadata
sample_data = b'Complex MP4 data with multiple tracks, chapters, and metadata'
file_path = './tmp/sample_complex_mp4.mp4'

# Track data
video_track_data = b'Video track data'
audio_track_data = b'Audio track data'
subtitle_track_data = b'Subtitle track data'

# Chapter data
chapter_data = b'Chapter data'

# Metadata
metadata = {
    'title': 'Complex MP4',
    'author': 'John Doe',
    'description': 'A sample mp4 file with complex structures'
}

with open(file_path, 'wb') as file:
    file.write(sample_data)
    file.write(video_track_data)
    file.write(audio_track_data)
    file.write(subtitle_track_data)
    file.write(chapter_data)

# Write metadata to a separate file
metadata_file_path = './tmp/sample_metadata.txt'
with open(metadata_file_path, 'w') as metadata_file:
    for key, value in metadata.items():
        metadata_file.write(f'{key}: {value}\n')

print(f"Generated MP4 file with multiple tracks, chapters, and metadata: {file_path}")
print(f"Metadata saved to: {metadata_file_path}")