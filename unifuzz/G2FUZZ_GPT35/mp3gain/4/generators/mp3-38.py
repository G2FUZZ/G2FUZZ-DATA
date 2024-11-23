import eyed3
import os

# Create a directory for storing the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Create a new mp3 file with additional complex features
with open('./tmp/generated_extended_features.mp3', 'w'):
    pass

# Load the created mp3 file with additional complex features
audio_file = eyed3.load('./tmp/generated_extended_features.mp3')

# Check if the audio_file is loaded successfully
if audio_file is not None:
    audio_file.initTag()

    # Set ID3 tags
    audio_file.tag.artist = 'Generated Artist'
    audio_file.tag.album = 'Generated Album'
    audio_file.tag.title = 'Generated Song'
    audio_file.tag.track_num = 1

    # Embed Lyrics
    lyrics = """These are the generated lyrics for the song.
    Lyrics line 1
    Lyrics line 2
    Lyrics line 3"""
    audio_file.tag.lyrics.set(lyrics)

    # Set Multiple Genres
    genres = ['Electronic', 'Ambient']
    audio_file.tag.frame_set['TCON'] = eyed3.id3.frames.TextFrame(b'\x00'.join(genres))

    # Save the changes
    audio_file.tag.save()
else:
    print("Error: Failed to load the audio file.")