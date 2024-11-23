import os
from pydub import AudioSegment

# Create a directory to store the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample audio with constant bit rate
audio = AudioSegment.silent(duration=5000)  # 5 seconds of silence
audio.export('./tmp/sample_cbr.mp3', format='mp3', bitrate='192k')