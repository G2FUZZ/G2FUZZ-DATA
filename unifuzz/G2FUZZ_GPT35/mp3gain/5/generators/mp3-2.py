import os
from mutagen.mp3 import EasyMP3

mp3_file_path = './tmp/sample.mp3'

if os.path.exists(mp3_file_path):
    mp3_file = EasyMP3(mp3_file_path)
    mp3_file['title'] = 'Sample Song'
    mp3_file['artist'] = 'John Doe'
    mp3_file['album'] = 'My Album'
    mp3_file['genre'] = 'Pop'
    mp3_file.save()
else:
    print(f"Error: File '{mp3_file_path}' not found.")