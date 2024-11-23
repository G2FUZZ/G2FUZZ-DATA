import eyed3
import os

# Create a directory for storing the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp3 file with metadata and chapter markers
audio_file = './tmp/sample_with_chapters.mp3'

# Check if the file exists before loading it
if os.path.exists(audio_file):
    audio = eyed3.load(audio_file)
    if audio is not None:
        audio.initTag()
        audio.tag.artist = 'John Doe'
        audio.tag.album = 'Sample Album'
        audio.tag.track_num = 1
        audio.tag.genre = 'Pop'

        # Adding Chapter markers
        chapter1 = eyed3.Chapter(title="Chapter 1", start_time=0)
        chapter2 = eyed3.Chapter(title="Chapter 2", start_time=60)  # Chapter starts at 1 minute (60 seconds)
        audio.tag.chapters.set([chapter1, chapter2])

        audio.tag.save()

        print(f"Generated mp3 file with metadata and chapter markers: {audio_file}")
    else:
        print(f"Error: Failed to load audio file: {audio_file}")
else:
    print(f"Error: Audio file not found: {audio_file}")