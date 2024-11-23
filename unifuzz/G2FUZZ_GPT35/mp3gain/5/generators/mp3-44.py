import os
from mutagen.mp3 import EasyMP3

def generate_mp3_file(file_path, metadata):
    if os.path.exists(file_path):
        for track_number, track_metadata in metadata.items():
            mp3_file = EasyMP3(file_path)
            mp3_file['title'] = track_metadata.get('title', 'Unknown Title')
            mp3_file['artist'] = track_metadata.get('artist', ['Unknown Artist'])
            mp3_file['album'] = track_metadata.get('album', 'Unknown Album')
            mp3_file['genre'] = track_metadata.get('genre', 'Unknown Genre')
            mp3_file['comment'] = track_metadata.get('comment', 'No comments')
            mp3_file['tracknumber'] = f"{track_number}/{len(metadata)}"
            mp3_file.save()
        print("MP3 files generated successfully!")
    else:
        print(f"Error: File '{file_path}' not found.")

# Define metadata for each track
metadata = {
    1: {
        'title': 'Track 1 Title',
        'artist': ['Artist A'],
        'album': 'Album X',
        'genre': 'Pop',
        'comment': 'This is a comment for Track 1.'
    },
    2: {
        'title': 'Track 2 Title',
        'artist': ['Artist B'],
        'album': 'Album Y',
        'genre': 'Rock',
        'comment': 'This is a comment for Track 2.'
    },
    3: {
        'title': 'Track 3 Title',
        'artist': ['Artist C'],
        'album': 'Album Z',
        'genre': 'Electronic',
        'comment': 'This is a comment for Track 3.'
    }
}

mp3_file_path = './tmp/sample_extended.mp3'
generate_mp3_file(mp3_file_path, metadata)