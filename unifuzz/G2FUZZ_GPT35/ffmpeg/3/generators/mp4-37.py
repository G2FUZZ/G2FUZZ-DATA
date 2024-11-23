import os

# Create a directory to store the generated mp4 files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp4 file with multiple tracks, subtitles, and chapters
video_track_1 = b'Video Track 1: Contains main video content'
video_track_2 = b'Video Track 2: Contains alternate angle video content'
audio_track_1 = b'Audio Track 1: Contains main audio content'
audio_track_2 = b'Audio Track 2: Contains alternate language audio content'
subtitles = b'Subtitles: English, Spanish'
chapters = b'Chapters: Chapter 1 - Introduction, Chapter 2 - Main Content, Chapter 3 - Conclusion'

with open('./tmp/sample_complex_mp4.mp4', 'wb') as f:
    f.write(b'\x00\x00\x00\x20\x66\x74\x79\x70\x6d\x70\x34\x32\x00\x00\x02\x00\x76\x69\x64\x65\x6d\x70\x34\x32\x00\x00\x00\x50\x6d\x76\x68\x64\x00\x00\x00\x00\x6d\x76\x68\x64\x00\x00\x00\x00' + video_track_1 + b'\x6d\x76\x68\x64\x00\x00\x00\x00' + video_track_2 + b'\x6d\x76\x68\x64\x00\x00\x00\x00' + audio_track_1 + b'\x6d\x76\x68\x64\x00\x00\x00\x00' + audio_track_2 + b'\x6d\x76\x68\x64\x00\x00\x00\x00' + subtitles + b'\x6d\x76\x68\x64\x00\x00\x00\x00' + chapters)