import eyed3
import os

# Create a directory for storing the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp3 file with metadata and cue sheet
audio_file = './tmp/sample_with_cue_sheet.mp3'

# Check if the file exists before loading it
if os.path.exists(audio_file):
    audio = eyed3.load(audio_file)
    if audio is not None:
        audio.initTag()
        audio.tag.artist = 'John Doe'
        audio.tag.album = 'Sample Album'
        audio.tag.track_num = 1
        audio.tag.genre = 'Pop'

        # Add cue sheet information
        cue_sheet = """
        REM GENRE Pop
        PERFORMER "John Doe"
        TITLE "Sample Track"
        FILE "sample.mp3" MP3
        TRACK 01 AUDIO
        TITLE "Sample Track"
        PERFORMER "John Doe"
        INDEX 01 00:00:00
        """
        audio.tag.cue = eyed3.cue.CueSheet()
        audio.tag.cue.parse(cue_sheet)

        audio.tag.save()

        print(f"Generated mp3 file with metadata and cue sheet: {audio_file}")
    else:
        print(f"Error: Failed to load audio file: {audio_file}")
else:
    print(f"Error: Audio file not found: {audio_file}")