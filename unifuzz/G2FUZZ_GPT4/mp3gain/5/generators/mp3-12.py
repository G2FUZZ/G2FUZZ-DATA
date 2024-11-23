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

# Bit rates to generate MP3 files for, including Layer III Audio Compression
bit_rates = ['8k', '128k', '320k']

# Extend the code to apply Layer III Audio Compression by leveraging the MP3 format's inherent compression capabilities.
# MP3 format is chosen for exporting, so by definition, it applies the Layer III Audio Compression.
for bit_rate in bit_rates:
    # Define the file path
    file_path = f'./tmp/tone_{bit_rate}_layer_iii.mp3'
    
    # Export the tone to an MP3 file with the specified bit rate
    tone.export(file_path, format="mp3", bitrate=bit_rate)

    print(f"Generated MP3 file with Layer III Audio Compression at {bit_rate} bitrate: {file_path}")