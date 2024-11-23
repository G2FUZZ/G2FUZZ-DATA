from pydub import AudioSegment
from pydub.generators import Sine
import numpy as np
import os

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate a 440 Hz sine wave (A4 note) for 5 seconds
frequency = 440  # Frequency in Hz
duration = 5000  # Duration in milliseconds
volume = -20.0  # Volume in dB

# Generate sine wave
tone = Sine(frequency, sample_rate=44100).to_audio_segment(duration=duration, volume=volume)

# Save the generated tone as an MP3 file
output_path = os.path.join(output_dir, 'generated_tone.mp3')
tone.export(output_path, format="mp3", bitrate="128k")

print(f"MP3 file saved to {output_path}")