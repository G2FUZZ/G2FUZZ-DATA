import os
import eyed3
from eyed3.id3.frames import ImageFrame
from pydub import AudioSegment

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a silent audio segment (10 seconds)
silence = AudioSegment.silent(duration=10000)

# Save the silent audio to an MP3 file
mp3_file_path = './tmp/silent_with_flags_and_psychoacoustic_model_and_crc.mp3'
silence.export(mp3_file_path, format="mp3", bitrate="192k")

# Load the MP3 file to edit its ID3 tags
audiofile = eyed3.load(mp3_file_path)

# If the file has no ID3 tag, create one
if audiofile.tag is None:
    audiofile.initTag()

audiofile.tag.title = "Silent Track with CRC"
audiofile.tag.artist = "Unknown Artist"
audiofile.tag.album = "Silent Album with CRC"

# Save the changes
audiofile.tag.save()

print(f"MP3 file saved at {mp3_file_path}")