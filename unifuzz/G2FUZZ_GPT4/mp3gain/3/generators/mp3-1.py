import os
from pydub import AudioSegment
from pydub.generators import Sine

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a 1-minute sine wave at 440 Hz (A4 - concert pitch)
duration_in_milliseconds = 60 * 1000  # 1 minute in milliseconds
frequency = 440  # Frequency in Hertz

# Generate sine wave
tone = Sine(frequency).to_audio_segment(duration=duration_in_milliseconds)

# Export to MP3 with default parameters which includes some level of compression
file_path = './tmp/sine_wave_440Hz.mp3'
tone.export(file_path, format="mp3")

print(f"Generated MP3 file saved at: {file_path}")