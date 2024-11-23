import os
import random

def generate_sample_data(size):
    return bytes([random.randint(0, 255) for _ in range(size)])

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp4 file with multiple tracks, subtitles, metadata, and chapters
video_track_data = generate_sample_data(1024)  # Sample video track data
audio_track_data = generate_sample_data(512)   # Sample audio track data
subtitle_data = b'Sample subtitles for the video'
metadata = {'title': 'Sample Video', 'creator': 'Generated Content Creator'}
chapters = ['Chapter 1: Intro', 'Chapter 2: Main Content', 'Chapter 3: Conclusion']

file_path = './tmp/sample_complex_mp4.mp4'

with open(file_path, 'wb') as file:
    file.write(video_track_data)
    file.write(audio_track_data)
    file.write(subtitle_data)
    # Write metadata to the file
    for key, value in metadata.items():
        file.write(f'{key}: {value}\n'.encode())
    # Write chapters to the file
    for chapter in chapters:
        file.write(f'Chapter: {chapter}\n'.encode())

print(f"Generated MP4 file with multiple video and audio tracks, subtitles, metadata, and chapters: {file_path}")