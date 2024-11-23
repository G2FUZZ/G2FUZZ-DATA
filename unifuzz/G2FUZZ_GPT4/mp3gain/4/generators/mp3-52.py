import numpy as np
from scipy.io.wavfile import write
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

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
        audio = np.vstack((audio, audio)).T
    return audio

def generate_complex_sound(frequencies, sample_rate, duration, volumes, pans):
    complex_sound = np.zeros((int(sample_rate * duration), 2), dtype=np.int16)
    for freq, volume, pan in zip(frequencies, volumes, pans):
        sound = generate_sine_wave(freq, sample_rate, duration, volume, pan)
        sound = sound.astype(np.int16)  # Ensure sound is np.int16
        complex_sound += sound
    return complex_sound

# Parameters for sound generation
sample_rate = 44100  # in Hz
duration = 5  # seconds
frequencies = [440, 554.37, 659.25]  # A4, C#5, E5
volumes = [0.8, 0.6, 0.4]
pans = [0.0, -0.5, 0.5]

# Generate a complex sound
complex_sound = generate_complex_sound(frequencies, sample_rate, duration, volumes, pans)

# Save the generated sound as a WAV file in the ./tmp/ directory
filename_wav = './tmp/complex_structure_sound.wav'
write(filename_wav, sample_rate, complex_sound)
print(f"Saved the audio file as {filename_wav}")