from pydub import AudioSegment
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a silent audio segment (10 seconds long)
silent_audio = AudioSegment.silent(duration=10000)  # Duration in milliseconds

# Export the silent audio as an MP3
file_path = './tmp/silent_with_metadata.mp3'
silent_audio.export(file_path, format="mp3", bitrate="192k", tags={"encoder": "LAME3.99r"})