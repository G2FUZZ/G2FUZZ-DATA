import eyed3
import os

# Create a directory for storing the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp3 file with metadata
audio_file = './tmp/sample.mp3'

# Check if the file exists before loading it
if os.path.exists(audio_file):
    audio = eyed3.load(audio_file)
    if audio is not None:
        audio.initTag()
        audio.tag.artist = 'John Doe'
        audio.tag.album = 'Sample Album'
        audio.tag.track_num = 1
        audio.tag.genre = 'Pop'
        audio.tag.save()

        print(f"Generated mp3 file with metadata: {audio_file}")
    else:
        print(f"Error: Failed to load audio file: {audio_file}")
else:
    print(f"Error: Audio file not found: {audio_file}")