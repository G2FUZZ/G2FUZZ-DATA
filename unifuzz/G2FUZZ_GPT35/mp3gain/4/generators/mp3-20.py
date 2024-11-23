import os
from pydub import AudioSegment

# Create a directory to store the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample audio with surround sound encoding
audio = AudioSegment.silent(duration=5000)  # 5 seconds of silence
audio = audio.set_channels(6)  # Set channels for surround sound (e.g., 5.1 or 7.1)
audio.export('./tmp/sample_surround_sound.mp3', format='mp3', bitrate='192k')