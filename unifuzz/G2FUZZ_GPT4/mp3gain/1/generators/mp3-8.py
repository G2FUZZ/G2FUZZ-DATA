from pydub import AudioSegment
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an audio segment of silence
silence = AudioSegment.silent(duration=1000)  # 1 second of silence

# Export the audio segment as an MP3 file
silence.export("./tmp/silent_mp3.mp3", format="mp3")

print("MP3 file generated without DRM.")