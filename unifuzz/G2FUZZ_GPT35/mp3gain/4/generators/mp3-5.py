import eyed3
import os

# Create a directory for storing the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Create a new mp3 file
with open('./tmp/generated.mp3', 'w'):
    pass

# Load the created mp3 file
audio_file = eyed3.load('./tmp/generated.mp3')

# Check if the audio_file is loaded successfully
if audio_file is not None:
    audio_file.initTag()

    # Set ID3 tags
    audio_file.tag.artist = 'Generated Artist'
    audio_file.tag.album = 'Generated Album'
    audio_file.tag.title = 'Generated Song'
    audio_file.tag.track_num = 1

    # Save the changes
    audio_file.tag.save()
else:
    print("Error: Failed to load the audio file.")