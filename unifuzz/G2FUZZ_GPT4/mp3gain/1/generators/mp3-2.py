import os
import numpy as np
from scipy.io.wavfile import write
from pydub import AudioSegment

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Parameters for the audio signal
sample_rate = 44100  # Sample rate in Hz
duration = 5  # Duration in seconds
frequency = 440  # Frequency of the sine wave in Hz

# Generate a sine wave for the given parameters
t = np.linspace(0, duration, int(sample_rate * duration), False)
audio_signal = np.sin(2 * np.pi * frequency * t)

# Convert the audio signal to 16-bit integers
audio_signal_int16 = np.int16(audio_signal * 32767)

# Save the audio signal to a WAV file
wav_file_path = './tmp/generated_audio.wav'
write(wav_file_path, sample_rate, audio_signal_int16)

# Convert the WAV file to MP3 with different bit rates
bit_rates = [128, 192, 256, 320]

for bit_rate in bit_rates:
    mp3_file_path = f'./tmp/generated_audio_{bit_rate}kbps.mp3'
    audio = AudioSegment.from_wav(wav_file_path)
    audio.export(mp3_file_path, format="mp3", bitrate=f"{bit_rate}k")

# Remove the temporary WAV file
os.remove(wav_file_path)