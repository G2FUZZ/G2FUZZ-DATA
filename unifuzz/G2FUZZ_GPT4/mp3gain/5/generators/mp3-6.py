import os
from pydub import AudioSegment
from pydub.generators import Sine

# Ensure the './tmp/' directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a sine wave audio segment
frequency = 440  # A4 note, in Hertz
duration_in_ms = 5000  # Duration in milliseconds
volume = -20.0  # Volume in dB

audio_segment = Sine(frequency).to_audio_segment(duration=duration_in_ms, volume=volume)

# Export the generated audio with a constant bitrate
file_path = './tmp/generated_audio.mp3'
# Use a common constant bitrate (CBR) for MP3
audio_segment.export(file_path, format="mp3", bitrate="192k")

print(f"Generated mp3 file at {file_path}")