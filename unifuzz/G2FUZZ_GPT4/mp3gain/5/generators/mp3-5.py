from pydub import AudioSegment
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TALB, TCON, TRCK, TYER, ID3NoHeaderError
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a silent audio segment (10 seconds long)
silent_audio = AudioSegment.silent(duration=10000)  # Duration in milliseconds

# Export the silent audio as an MP3
file_path = './tmp/silent_with_metadata.mp3'
silent_audio.export(file_path, format="mp3")

try:
    # Load the ID3 tag from the file, or create a new one if it doesn't exist
    tags = ID3(file_path)
except ID3NoHeaderError:
    print("Adding ID3 header;")
    tags = ID3()

# Add metadata
tags["TIT2"] = TIT2(encoding=3, text='Silent Track')
tags["TPE1"] = TPE1(encoding=3, text='Silent Artist')
tags["TALB"] = TALB(encoding=3, text='Silent Album')
tags["TCON"] = TCON(encoding=3, text='Silence')
tags["TRCK"] = TRCK(encoding=3, text='1')
tags["TYER"] = TYER(encoding=3, text='2023')

# Save the tags back to the file
tags.save(file_path)

print("MP3 with metadata generated successfully.")