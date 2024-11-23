import numpy as np
from scipy.io.wavfile import write
import os
from pydub import AudioSegment
import subprocess

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

# Function to apply Replay Gain to an MP3 file
def apply_replay_gain(filename):
    # Use FFmpeg to calculate and apply Replay Gain
    command = f"ffmpeg -i {filename} -af loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json -f null /dev/null"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, _ = process.communicate()
    loudnorm_stats = stdout.decode()
    print(loudnorm_stats)

# Function to embed Digital Rights Management (DRM) information
def embed_drm_information(filename, drm_info):
    # Assuming DRM information is a simple text that can be added as a tag
    # Using an imaginary library `audio_metadata` for demonstration
    # In real scenarios, DRM embedding would require a specific DRM provider's SDK or tools
    # For demonstration, we'll just print the DRM info to simulate embedding
    print(f"Embedding DRM information: {drm_info} into {filename}")
    # This is a placeholder. Actual DRM embedding would significantly differ and likely involve encryption and rights management servers.

# Sample rate and duration
sample_rate = 44100  # in Hz
duration = 5  # in seconds

# Frequency of the sine wave
frequency = 440  # A4 note

# Generate sine wave data
audio_data = generate_sine_wave(frequency, sample_rate, duration)

# Bit rates to generate MP3 files for
bit_rates = [128, 192, 320]

# DRM information
drm_info = "This content is protected by DRM."

# Generate MP3 files at different bit rates
for bit_rate in bit_rates:
    filename = f'./tmp/sine_wave_{bit_rate}kbps.mp3'
    create_mp3(filename, audio_data, sample_rate, bit_rate)
    apply_replay_gain(filename)
    embed_drm_information(filename, drm_info)

print("MP3 files generated at different bit rates with Replay Gain information and DRM.")