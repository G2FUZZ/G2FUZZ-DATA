import os
from mutagen.mp3 import EasyMP3

mp3_file_path = './tmp/sample_extended.mp3'

if os.path.exists(mp3_file_path):
    mp3_file = EasyMP3(mp3_file_path)
    mp3_file['title'] = 'Sample Extended Song'
    mp3_file['artist'] = ['John Doe', 'Jane Smith']
    mp3_file['album'] = 'My Extended Album'
    mp3_file['genre'] = 'Pop'
    mp3_file['comment'] = 'This is a custom comment for the song.'
    mp3_file['tracknumber'] = '1/10'
    mp3_file.save()
else:
    print(f"Error: File '{mp3_file_path}' not found.")