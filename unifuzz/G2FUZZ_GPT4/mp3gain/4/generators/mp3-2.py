import numpy as np
from scipy.io.wavfile import write
import os
from pydub import AudioSegment

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a sine wave
def generate_sine_wave(freq, sample_rate, duration):
    t = np.linspace(0, duration, int(sample_rate*duration), False)
    note = np.sin(freq * t * 2 * np.pi)
    audio_data = note * (2**15 - 1) / np.max(np.abs(note))
    return audio_data.astype(np.int16)

# Function to create an MP3 file from numpy array data
def create_mp3(filename, audio_data, sample_rate, bit_rate):
    # Save the audio data to a temporary WAV file
    temp_filename = filename + '.wav'
    write(temp_filename, sample_rate, audio_data)
    # Convert the WAV file to MP3
    audio = AudioSegment.from_wav(temp_filename)
    audio.export(filename, format='mp3', bitrate=f'{bit_rate}k')
    # Remove the temporary WAV file
    os.remove(temp_filename)

# Sample rate and duration
sample_rate = 44100  # in Hz
duration = 5  # in seconds

# Frequency of the sine wave
frequency = 440  # A4 note

# Generate sine wave data
audio_data = generate_sine_wave(frequency, sample_rate, duration)

# Bit rates to generate MP3 files for
bit_rates = [128, 192, 320]

# Generate MP3 files at different bit rates
for bit_rate in bit_rates:
    filename = f'./tmp/sine_wave_{bit_rate}kbps.mp3'
    create_mp3(filename, audio_data, sample_rate, bit_rate)

print("MP3 files generated at different bit rates.")