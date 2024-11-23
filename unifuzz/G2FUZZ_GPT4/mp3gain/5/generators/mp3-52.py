from pydub import AudioSegment
from pydub.generators import Sine
import os

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Parameters for the stereo audio
duration_in_seconds = 10  # Duration of the audio file in seconds
left_frequency_hz = 440  # Frequency of the sine wave for the left channel (A4 pitch)
right_frequency_hz = 554.37  # Frequency of the sine wave for the right channel (C#5 pitch)
sample_rate = 44100  # Sample rate
volume = -3.0  # Volume

# Generate a sine wave tone for the left and right channels
left_tone = Sine(left_frequency_hz, sample_rate=sample_rate).to_audio_segment(duration=duration_in_seconds * 1000, volume=volume)
right_tone = Sine(right_frequency_hz, sample_rate=sample_rate).to_audio_segment(duration=duration_in_seconds * 1000, volume=volume)

# Create a stereo sound from the left and right tones
stereo_sound = AudioSegment.from_mono_audiosegments(left_tone, right_tone)

# Bit rates to generate MP3 files for
bit_rates = ['8k', '128k', '320k']

for bit_rate in bit_rates:
    # Define the file path
    file_path = f'./tmp/stereo_tone_{bit_rate}.mp3'
    
    # Export the stereo sound to an MP3 file with the specified bit rate
    tags = {
        'artist': 'Example Artist',
        'album': 'Example Album',
        'comments': 'This file was generated using PyDub.'
    }
    # Temporarily remove the cover parameter to test if it's causing the issue
    stereo_sound.export(file_path, format="mp3", bitrate=bit_rate, tags=tags)

    print(f"Generated stereo MP3 file at {bit_rate} bitrate with metadata: {file_path}")