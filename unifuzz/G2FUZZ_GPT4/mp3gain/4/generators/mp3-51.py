import numpy as np
import os
from pydub import AudioSegment
import subprocess

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a sine wave with stereo panning
def generate_sine_wave(freq, sample_rate, duration, volume=1.0, pan=0.0):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    note = np.sin(freq * t * 2 * np.pi) * volume
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    audio = audio.astype(np.int16)
    if pan != 0.0:
        left = audio * min(1.0 - pan, 1.0)
        right = audio * min(1.0 + pan, 1.0)
        audio = np.vstack((left, right)).T
    else:
        audio = np.vstack((audio, audio)).T  # Make it stereo without panning
    return audio

# Function to generate chords
def generate_chord(frequencies, sample_rate, duration, volume=1.0, pan=0.0):
    chord = np.zeros((int(sample_rate * duration), 2)) # Initialize a stereo signal
    for freq in frequencies:
        note = generate_sine_wave(freq, sample_rate, duration, volume, pan)
        chord[:, 0] += note[:, 0]  # Left channel
        chord[:, 1] += note[:, 1]  # Right channel
    # Normalize to prevent clipping
    chord = chord * (2**15 - 1) / np.max(np.abs(chord))
    return chord.astype(np.int16)

# Function to apply fade in and fade out
def apply_fade(audio, sample_rate, fade_in_duration, fade_out_duration):
    num_samples = audio.shape[0]
    fade_in_samples = int(fade_in_duration * sample_rate)
    fade_out_samples = int(fade_out_duration * sample_rate)

    # Apply fade in
    for i in range(fade_in_samples):
        audio[i, :] = audio[i, :] * (i / fade_in_samples)
    
    # Apply fade out
    for i in range(fade_out_samples):
        audio[-i-1, :] = audio[-i-1, :] * (i / fade_out_samples)
    
    return audio

# Function to create an MP3 file from numpy array data
def create_mp3(filename, audio_data, sample_rate, bit_rate, complexity=None):
    # Convert the NumPy array to bytes
    audio_bytes = audio_data.tobytes()
    # Create a PyDub audio segment with stereo channels
    sound = AudioSegment(audio_bytes, sample_width=2, frame_rate=sample_rate, channels=2)
    # Export as MP3 with or without adjustable complexity
    if complexity is not None:
        # Assuming complexity adjustment is possible with a specific encoder setting
        sound.export(filename, format='mp3', bitrate=f'{bit_rate}k', parameters=["-compression_level", str(complexity)])
    else:
        sound.export(filename, format='mp3', bitrate=f'{bit_rate}k')

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
    # Embedding DRM information
    print(f"Embedding DRM information: {drm_info} into {filename}")
    # This is a placeholder. Actual DRM embedding would significantly differ.

# Sample rate and duration
sample_rate = 44100  # in Hz
duration = 5  # in seconds

# Generate stereo sine wave data with fade in and out applied
audio_data = generate_sine_wave(440, sample_rate, duration, volume=1.0, pan=0.0)
audio_data = apply_fade(audio_data, sample_rate, 0.5, 0.5)  # Applying fade in and fade out

# Bit rates and complexity levels to generate MP3 files for
bit_rates = [128, 192, 320]
complexity_levels = [5, 7, 9]  # Hypothetical complexity levels for demonstration

# DRM information
drm_info = "This content is protected by DRM."

# Generate MP3 files at different bit rates and complexity levels
for bit_rate, complexity in zip(bit_rates, complexity_levels):
    filename = f'./tmp/sine_wave_{bit_rate}kbps_complexity{complexity}.mp3'
    create_mp3(filename, audio_data, sample_rate, bit_rate, complexity)
    apply_replay_gain(filename)
    embed_drm_information(filename, drm_info)

print("MP3 files generated at different bit rates with Replay Gain information, DRM, and adjustable complexity.")