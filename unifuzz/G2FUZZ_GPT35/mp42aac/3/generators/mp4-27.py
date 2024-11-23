import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a complex MP4 file with multiple tracks and metadata
file_path = './tmp/complex_video.mp4'

# Simulate video data for different tracks
video_track_1_data = b'Video Track 1 Data'
video_track_2_data = b'Video Track 2 Data'
audio_track_data = b'Audio Track Data'

# Simulate metadata information
metadata = {
    'title': 'Complex Video File',
    'author': 'John Doe',
    'creation_date': '2022-01-01'
}

# Write the complex MP4 file
with open(file_path, 'wb') as file:
    file.write(video_track_1_data)  # Write Video Track 1 data
    file.write(audio_track_data)    # Write Audio Track data
    file.write(video_track_2_data)  # Write Video Track 2 data

    # Write metadata as XML format at the end of the file
    metadata_str = '<?xml version="1.0" encoding="UTF-8"?>\n<metadata>\n'
    for key, value in metadata.items():
        metadata_str += f'\t<{key}>{value}</{key}>\n'
    metadata_str += '</metadata>'
    file.write(metadata_str.encode())

print(f'Generated complex MP4 file with multiple tracks and metadata: {file_path}')