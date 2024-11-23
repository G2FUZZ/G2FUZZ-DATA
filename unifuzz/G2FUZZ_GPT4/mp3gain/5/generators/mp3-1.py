from pydub import AudioSegment
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a 5-second silent audio segment
silent_audio = AudioSegment.silent(duration=5000)  # Duration in milliseconds

# Export the audio segment as an MP3 file
file_path = './tmp/silent_audio.mp3'
silent_audio.export(file_path, format="mp3")

print(f"MP3 file has been saved to: {file_path}")