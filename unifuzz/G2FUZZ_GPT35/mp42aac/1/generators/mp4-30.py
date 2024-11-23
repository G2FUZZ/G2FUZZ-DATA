import os
import random

# Create a directory to store the generated 'mp4' files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample 'mp4' file with multiple video and audio tracks, subtitles, and metadata
file_path = './tmp/complex_mp4_example.mp4'

# Simulate multiple video and audio tracks
video_tracks = ['Video Track 1', 'Video Track 2']
audio_tracks = ['Audio Track 1', 'Audio Track 2']

# Simulate subtitles
subtitles = ['English Subtitles', 'French Subtitles']

# Simulate metadata
metadata = {'title': 'Complex MP4 Example', 'year': 2021, 'duration': '00:05:30'}

# Write simulated data to the mp4 file
with open(file_path, 'w') as f:
    f.write(f"Video Tracks: {', '.join(video_tracks)}\n")
    f.write(f"Audio Tracks: {', '.join(audio_tracks)}\n")
    f.write(f"Subtitles: {', '.join(subtitles)}\n")
    f.write(f"Metadata: {metadata}\n")

print(f"Generated 'mp4' file with multiple video and audio tracks, subtitles, and metadata: {file_path}")