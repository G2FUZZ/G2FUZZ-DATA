import numpy as np
from scipy.io.wavfile import write
import os
from pydub import AudioSegment

# Ensure the tmp directory exists
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Function to generate a sine wave
def generate_sine_wave(freq, sample_rate, duration):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    note = np.sin(freq * t * 2 * np.pi)
    # Normalize to 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    return audio.astype(np.int16)

# Function to save the sine wave as an MP3 file
def save_as_mp3(audio, sample_rate, filename):
    # Save the generated audio as a WAV file first
    wav_file = filename.replace('.mp3', '.wav')
    write(wav_file, sample_rate, audio)
    # Convert the WAV to MP3
    sound = AudioSegment.from_wav(wav_file)
    sound.export(filename, format="mp3")
    # Remove the WAV file
    os.remove(wav_file)

# Define parameters
frequencies = [440]  # A4
durations = [2]  # 2 seconds
sample_rates = [44100, 48000]  # 44.1 kHz, 48 kHz

# Generate and save MP3 files
for sample_rate in sample_rates:
    for freq in frequencies:
        for duration in durations:
            filename = f'./tmp/sine_{freq}Hz_{sample_rate}Hz_{duration}s.mp3'
            audio = generate_sine_wave(freq, sample_rate, duration)
            save_as_mp3(audio, sample_rate, filename)
            print(f"Generated {filename}")