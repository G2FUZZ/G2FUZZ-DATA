import numpy as np
from pydub import AudioSegment
from pydub.generators import Sine
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a 1-second sine wave at 440 Hz
tone = Sine(440).to_audio_segment(duration=1000)

# Save the generated sine wave to a file
file_path = './tmp/original_tone.mp3'
tone.export(file_path, format="mp3")

# Load the MP3 file
audio = AudioSegment.from_mp3(file_path)

# Normalize the audio to a standard volume level
normalized_audio = audio.apply_gain(-audio.dBFS)

# Save the normalized audio
normalized_file_path = './tmp/normalized_tone.mp3'
normalized_audio.export(normalized_file_path, format="mp3")

print(f"Original and normalized MP3 files saved to './tmp/'")