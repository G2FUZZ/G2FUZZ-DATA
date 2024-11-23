import numpy as np
from scipy.io.wavfile import write
import os
from pydub import AudioSegment

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Parameters for the audio file
sample_rate = 44100  # Sample rate in Hz
duration = 10  # Duration in seconds
frequency = 440  # Frequency of the sine wave in Hz

# Generate the sine wave
t = np.linspace(0, duration, int(sample_rate * duration), False)  # Time axis
audio = np.sin(2 * np.pi * frequency * t) * 0.3  # Generate sine wave

# Convert to 16-bit signed integers
audio = np.int16(audio * 32767)

# Save the sine wave as a WAV file first
wav_path = './tmp/example.wav'
write(wav_path, sample_rate, audio)

# Convert the WAV file to MP3
audio_segment = AudioSegment.from_wav(wav_path)
mp3_path = './tmp/example.mp3'
audio_segment.export(mp3_path, format="mp3")

# Clean up the WAV file as it's no longer needed
os.remove(wav_path)

print(f"MP3 file saved to {mp3_path}")