from pydub import AudioSegment
from pydub.generators import Sine

# Ensure the tmp directory exists
import os
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Generate a 5-second sine wave tone at 440 Hz
tone_duration_ms = 5000  # Duration in milliseconds
frequency_hz = 440  # Frequency in Hertz
sine_wave = Sine(frequency_hz).to_audio_segment(duration=tone_duration_ms)

# Export the audio segment without VBR to test
file_path = './tmp/sine_wave.mp3'
# Specify a constant bitrate (CBR) instead of VBR to avoid the error
sine_wave.export(file_path, format="mp3", bitrate="192k")

print(f"File has been saved to {file_path}")