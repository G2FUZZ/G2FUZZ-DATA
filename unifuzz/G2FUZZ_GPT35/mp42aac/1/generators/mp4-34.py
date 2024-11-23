import os

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp4 file with multiple video tracks, audio tracks, and metadata
sample_data = b'Fake MP4 data with multiple video tracks, audio tracks, and metadata'
file_path = './tmp/sample_complex_mp4_file.mp4'

# Simulate multiple video tracks, audio tracks, and metadata information
video_track_1 = b'Video Track 1 data'
video_track_2 = b'Video Track 2 data'
audio_track = b'Audio Track data'
metadata = {
    'title': 'Sample Video',
    'duration': '10:30',
    'resolution': '1080p'
}

with open(file_path, 'wb') as file:
    # Write video tracks
    file.write(video_track_1)
    file.write(video_track_2)
    
    # Write audio track
    file.write(audio_track)
    
    # Write metadata information
    for key, value in metadata.items():
        file.write(f'{key}: {value}\n'.encode())

print(f"Generated complex MP4 file with multiple video tracks, audio tracks, and metadata: {file_path}")