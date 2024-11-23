from pydub import AudioSegment
from pydub.generators import Sine
import os

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Parameters for the audio
duration_in_seconds = 10  # Duration of the audio file in seconds
frequency_hz = 440  # Frequency of the sine wave (A4 pitch)
sample_rate = 44100  # Sample rate

# Generate a sine wave tone with the specified sample rate
tone = Sine(frequency_hz, sample_rate=sample_rate).to_audio_segment(duration=duration_in_seconds * 1000, volume=-3.0)

# Bit rates to generate MP3 files for
bit_rates = ['8k', '128k', '320k']

for bit_rate in bit_rates:
    # Define the file path
    file_path = f'./tmp/tone_{bit_rate}.mp3'
    
    # Export the tone to an MP3 file with the specified bit rate
    tone.export(file_path, format="mp3", bitrate=bit_rate)

    print(f"Generated MP3 file at {bit_rate} bitrate: {file_path}")